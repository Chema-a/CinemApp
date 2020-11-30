import { Component, OnInit } from '@angular/core';
import { PeliculasService } from '../api/peliculas.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit{
  peliculas = [];

  constructor(private peliculasService: PeliculasService) {}
  ngOnInit(){
    this.peliculasService.peliculas.subscribe(peliculas =>{
     this.peliculas = peliculas; 
    });
    this.peliculasService.getPeliculas();
  }

}
