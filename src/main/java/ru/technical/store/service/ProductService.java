package ru.technical.store.service;

import ru.technical.store.entity.Product;
import ru.technical.store.exception.ProductNotFoundException;
import ru.technical.store.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductService {

  private final ProductRepository repository;
  private final CartService cartService;

  @Autowired
  public ProductService(ProductRepository repository, CartService cartService) {
    this.repository = repository;
    this.cartService = cartService;
  }

  public void saveProduct(Product product) {
    repository.save(product);
  }

  public Product getProductById(Long id) {
    return repository.findById(id).orElseThrow(() -> new ProductNotFoundException(id));
  }

  public List<Product> getAllProducts() {
    return repository.findAll();
  }

  public Page<Product> getPaginatedProducts(int page, int pageSize) {
    return repository.findAll(PageRequest.of(page - 1, pageSize));
  }

  public List<Product> getAllByCategoryAndTitle(String category, String title) {
    // trim() вызывается, чтобы отсечь лишние проблемы у запрашиваемого title
    return repository.findProductsByCategoryNameAndContainsTitle(category, title.trim());
  }

  public void deleteProductById(Long id) {
    cartService.getAllCarts().forEach(cart -> cart.getProducts().remove(getProductById(id)));
    repository.deleteById(id);
  }
}
