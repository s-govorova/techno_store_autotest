package ru.technical.store.repository;

import ru.technical.store.entity.Category;
import ru.technical.store.entity.Product;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.math.BigDecimal;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

@SpringBootTest
class ProductRepositoryTest {

    @Autowired
    private ProductRepository productRepository;
    @Autowired
    private CategoryRepository categoryRepository;

    @Test
    void find_product_by_title_and_category() {
        Category category = new Category("smart");
        Product product = new Product("LG", "test", category, new BigDecimal(1000), 0);

        categoryRepository.save(category);
        productRepository.save(product);

        assertFalse(productRepository.findProductsByCategoryNameAndContainsTitle(category.getCategoryName(), "LG").isEmpty());
        assertFalse(productRepository.findProductsByCategoryNameAndContainsTitle(category.getCategoryName(), "lg").isEmpty());
        assertTrue(productRepository.findProductsByCategoryNameAndContainsTitle("not category", "lg").isEmpty());
    }
}