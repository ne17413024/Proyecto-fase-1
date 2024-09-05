Funcion venta
	estado<-Booleano
    Definir producto_vender Como Cadena
	encontrado<-Booleano
    Definir precio Como Real
    Definir categoria_nombre Como Cadena
    Definir i Como Entero
	
	
	
    Escribir "\nCategorías y productos disponibles:"
	
    // Mostrar categorías y productos
    Para cada categoria En productos Hacer
		categoria_nombre<-categoria
        Escribir "\nCategoría: ", categoria_nombre
        
        Escribir "Productos:"
    
    FinPara
	
	Escribir "Ingresa los productos a vender uno por uno ingresa * para salir"
	
    estado <- Verdadero
	productos_vendidos<-ListaVacia
    total1 <- 0.0
	
    Mientras estado Hacer
        
		
		
		
        Si producto_vender = "*" Entonces
            estado <- Falso
        Sino
            encontrado <- Falso
            Para cada categoria En productos Hacer
      
                FinPara
                Si encontrado Entonces
                    //Salir
                FinSi
          
            
            Si No encontrado Entonces
                
            FinSi
        FinSi
    FinMientras
	
    Escribir "\nProductos vendidos:"
    Para cada item En productos_vendidos Hacer
     
        Escribir "  - ", producto, ": $", precio
    FinPara
	
    Escribir "\nTotal de la venta: $", total
FinFuncion



Proceso SistemaDeVentas
	productos <- matriz
	productos_vendidos <- lista
	total <- 0
FinProceso
