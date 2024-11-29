// Importación de dependencias necesarias
import { defineStore } from 'pinia'; // 'defineStore' se usa para definir una tienda (store) con Pinia.
import axios, { AxiosError } from 'axios'; // 'axios' es para hacer peticiones HTTP, 'AxiosError' es para manejar errores de Axios.

const UserAuth = defineStore('UserAuth', {

  state: () => {
    return {
      mensaje: '' as string | null, // Mensaje de error o éxito en la autenticación.
      errores: null as number | null, // Código de error HTTP (si ocurre uno).
      token: null as string | null, // Almacena el token de autenticación del usuario.
      status : null as number | null
    }
  },
  actions: {
    async login(username: string, password: string, rememberMe: boolean) {
      try {
        // Realiza la solicitud POST a la API para obtener el token
        const response: any = await axios.post('/api/token/', {
          username,
          password, 
        });
        // Si la autenticación es exitosa, se asigna el token al estado de la tienda
        this.token = response.data.access;
        // Si la opción 'rememberMe' es verdadera, almacena el token en localStorage
        if (rememberMe == true) {
          localStorage.setItem('token', response.data.access);
        }
        // Limpia cualquier error previo
        this.errores = null;
        // Retorna un objeto de éxito
        return { success: true };
      } catch (error) {
        // Manejo de errores si la autenticación falla
        const axiosError = error as AxiosError; // Convierte el error en un tipo AxiosError

        // Si la respuesta del servidor tiene un error (código >= 400), maneja el error
        if (axiosError.response && axiosError.response.status >= 400) {
          this.errores = axiosError.response.status; // Almacena el código de error HTTP
          
          // Extrae el mensaje de error desde la respuesta de la API (si está disponible)
          const responseData = axiosError.response.data as ErrorResponse;
          this.mensaje = responseData.detail ?? null; // Si no hay mensaje, asigna null
        } else {
          // Si el error no tiene respuesta o es un error inesperado
          this.errores = 500; // Asigna un código de error genérico (500)
          this.mensaje = "A sucedido un error inesperado"; // Mensaje genérico de error
        }

        // Retorna un objeto con el estado de error y el mensaje correspondiente
        return { success: false, error: this.mensaje };
      }
    },
    logout() {
      this.token = null;
      localStorage.removeItem('token');
      sessionStorage.removeItem('token');
      return { success: true };
    },
    async register(username: string, email: string, password: string, password2: string, last_name: string, first_name: string){
      try {
        const response: any = await axios.post('/register/', {
          username,
          email,
          password,
          password2,
          last_name,
          first_name,
        });
        return { success: true };
      } catch (error) {
        const axiosError = error as AxiosError;

        if (axiosError.response && axiosError.response.status >= 400) {
          const responseData = axiosError.response.data as Record<string, any>;
          if (responseData.username) {
              this.mensaje = 'El nombre de usuario ya está en uso.';
          } else if (responseData.email) {
              this.mensaje = 'El correo ya está registrado.';
          } else {
              this.mensaje = responseData.detail ?? 'Error desconocido.';
          }
          this.errores = axiosError.response.status;
      } else {
          this.errores = 500;
          this.mensaje = 'Ha ocurrido un error inesperado.';
      }
      return { success: false, error: this.mensaje };
      }
    }
  }
})

// Exporta la tienda para poder usarla en otros componentes
export default UserAuth;

// Definición de la interfaz para la respuesta de error de la API
interface ErrorResponse {
  detail?: string; // La propiedad 'detail' contiene el mensaje de error, si está presente
}
