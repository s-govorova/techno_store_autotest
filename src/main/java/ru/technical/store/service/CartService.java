package ru.technical.store.service;

import ru.technical.store.entity.Cart;
import ru.technical.store.entity.Product;
import ru.technical.store.exception.CartNotFoundException;
import ru.technical.store.exception.UserNotFoundException;
import ru.technical.store.repository.CartRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.List;

@Service
public class CartService {

  private final CartRepository cartRepository;
  private final UserService userService;

  @Autowired
  public CartService(CartRepository cartRepository, UserService userService) {
    this.cartRepository = cartRepository;
    this.userService = userService;
  }

  public void saveCart(Cart cart) {
    cartRepository.save(cart);
  }

  public Cart getCartById(Long id) {
    return cartRepository.findById(id).orElseThrow(() -> new CartNotFoundException(id));
  }

  public List<Cart> getAllCarts() {
    return cartRepository.findAll();
  }

  public Cart getCartByUserId(Long id) {
    return cartRepository.findCartByUserId(id).orElseThrow(() -> new UserNotFoundException(id));
  }

  public BigDecimal getTotalPriceCart() {
    return getLoggedUserCart().getProducts().stream()
        .map(Product::getPrice)
        .reduce(BigDecimal.ZERO, BigDecimal::add);
  }

  public Cart getLoggedUserCart() {
    return getCartByUserId(userService.getLoggedUser().getId());
  }

  public void addProductToCart(Product product) {
    getLoggedUserCart().getProducts().add(product);
    cartRepository.save(getLoggedUserCart());
  }

  public void deleteProductFromCart(Product product) {
    getLoggedUserCart().getProducts().remove(product);
    cartRepository.save(getLoggedUserCart());
  }
}
