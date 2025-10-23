package ru.technical.store.service;

import ru.technical.store.entity.Category;
import ru.technical.store.entity.Product;
import ru.technical.store.exception.CategoryIsNotEmptyException;
import ru.technical.store.exception.CategoryNotFoundException;
import ru.technical.store.repository.CategoryRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
class CategoryServiceTest {

    @Mock
    private CategoryRepository categoryRepository;

    @InjectMocks
    private CategoryService categoryService;

    @Test
    public void saveCategory() {
        Category category = new Category("smart");

        when(categoryRepository.save(any(Category.class))).thenReturn(category);
        categoryService.saveCategory(category);

        when(categoryRepository.findById(1L)).thenReturn(Optional.of(category));
        Category found = categoryService.getCategoryById(1L);

        assertThat(found).isNotNull(); // Сохраняем объект, а потом получаем его. Проверяем на null и равенство полей
        assertThat(found).isEqualTo(category);

    }

    @Test
    void getCategoryById() {
        when(categoryRepository.findById(1L)).thenReturn(Optional.of(new Category("smart")));
        categoryService.getCategoryById(1L);
        assertDoesNotThrow(() -> new CategoryNotFoundException(1L));

        when(categoryRepository.findById(2L)).thenThrow(new CategoryNotFoundException(2L)); // Если категория не найдена, кидаем exception
        assertThrows(CategoryNotFoundException.class, () -> categoryService.getCategoryById(2L));

    }

    @Test
    void getAllCategories() {
        Category category = new Category("smart");
        List<Category> categories = new ArrayList<>();
        categories.add(category);

        when(categoryRepository.findAll()).thenReturn(categories);
        List<Category> found = categoryService.getAllCategories();
        verify(categoryRepository).findAll();

        assertThat(found).isNotNull();
        assertThat(found.size()).isEqualTo(1);
        assertThat(found.get(0)).isEqualTo(category);
    }

    @Test
    void deleteById() {
        Category category = new Category("smart");
        when(categoryRepository.findById(1L)).thenReturn(Optional.of(category)).thenReturn(null); // Чтобы категорию можно было удалить, инициализируем её
        categoryService.deleteById(1L); // Тест: удаление категории
        verify(categoryRepository).deleteById(1L);

        Product productInCategory = new Product("LG", "test", category, new BigDecimal(1000), 0);
        category.setProducts(Set.of(productInCategory)); // Назначаем товар категории

        when(categoryRepository.findById(2L)).thenReturn(Optional.of(category));
        assertThrows(CategoryIsNotEmptyException.class, () -> categoryService.deleteById(2L)); // Тест: удаление непустой
    }                                                                                          // категори должно выбрасывать exception
}