import { Component,OnInit} from '@angular/core';
import {  ProductService } from '../../services/product.service';
import { Product } from '../../services/product.model';
import { NgIf } from '@angular/common';
import { NgFor } from '@angular/common';
@Component({
  selector: 'app-home-a',
  standalone: true,
  imports: [NgFor,NgIf],
  templateUrl: './home-a.component.html',
  styleUrl: './home-a.component.css'
})
export class HomeAComponent implements OnInit {
  products: Product[]=[];
  totalAmount: number = 0;

  constructor(private productService: ProductService) { }

  ngOnInit(): void {
    this.fetchProducts();
  }

  fetchProducts() {
    this.productService.getProducts()
      .subscribe(products => {
        this.products = products;
        this.calculateTotalAmount();
      });
  }

  calculateTotalAmount() {
    this.totalAmount = this.products.reduce((total, product) => total + product.price, 0);
  }
}