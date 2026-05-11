package com.ecommerce;

import com.ecommerce.entity.Product;
import com.ecommerce.repository.ProductRepository;
import com.ecommerce.service.ProductService;

import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class ProductServiceTest {

    @Test
    void testGetAllProducts() {

        ProductRepository repository = Mockito.mock(ProductRepository.class);

        Mockito.when(repository.findAll())
                .thenReturn(List.of(
                        new Product(1L,"Laptop","Gaming",50000,2)
                ));

        ProductService service = new ProductService(repository);

        assertEquals(1, service.getAllProducts().size());
    }
}
