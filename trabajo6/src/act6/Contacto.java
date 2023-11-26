package Act6;

import java.io.Serializable;

// Clase que representa un contacto serializable
public class Contacto implements Serializable {
    // Atributos privados para el nombre y el número de teléfono
    private String name;
    private String number;

    // Constructor que inicializa un contacto con un nombre y un número de teléfono
    public Contacto(String name, String number) {
        this.name = name;
        this.number = number;
    }

    // Método para obtener el nombre del contacto
    public String getName() {
        return name;
    }

    // Método para obtener el número de teléfono del contacto
    public String getNumber() {
        return number;
    }

    // Método para establecer el número de teléfono del contacto
    public void setNumber(String number) {
        this.number = number;
    }

    // Método override de toString para obtener una representación de cadena del contacto
    @Override
    public String toString() {
        return "Contact{name='" + name + "', number='" + number + "'}";
    }
}
