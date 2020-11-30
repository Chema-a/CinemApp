import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Subject } from 'rxjs'; /*Biblioteca para programación reactiva*/

@Injectable({
  providedIn: 'root'
})
export class PeliculasService {
  peliculas = new Subject<any[]>();

  constructor(private http:HttpClient) { 
    this.getPeliculas();
  }

  getPeliculas(){
    this.http.get<any[]>("/api/v1/peliculas").subscribe(data => {
      this.peliculas.next(data);
    });
  }
}
