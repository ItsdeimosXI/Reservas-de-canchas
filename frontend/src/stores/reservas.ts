import { defineStore } from "pinia";

import axios, { AxiosError } from 'axios';

const Reservas = defineStore('Reservas', {
    state: () => {
        return {
            mensaje: '' as string | null, // Mensaje de error o éxito.
            errores: null as number | null, // Código de error HTTP (si ocurre uno).
            token: null as string | null, // Almacena el token de autenticación del usuario.
            status: null as number | null,
            canchas: null as Array<any> | null
        }
    },

    actions: {
       async GetCanchas(){
        try{
        const response = await axios.get('/api/canchas/')
        this.canchas = response.data.results;
        return {success: true}
        }catch(error){
            const axiosError = error as AxiosError;
            if (axiosError.response && axiosError.response.status >=400){
                this.errores = axiosError.response.status

                const responseData = axiosError.response.data as ErrorResponse;
                this.mensaje = responseData.detail ?? null;
            }else{
                this.errores = 500;
                this.mensaje = "A sucedido un error inesperado";
            }
            return {success: false, error: this.mensaje}
        }
       
       },
       async GetCanchasByID(id:any){
        try{
        const response = await axios.get('/api/canchas/' + id + '/')
        this.canchas = response.data;
        return {success: true}
        }catch(error){
            const axiosError = error as AxiosError;
            if (axiosError.response && axiosError.response.status >=400){
                this.errores = axiosError.response.status
                const responseData = axiosError.response.data as ErrorResponse;
                this.mensaje = responseData.detail ?? null;
            }else{
                this.errores = 500;
                this.mensaje = "A sucedido un error inesperado";
            }
            return {success: false, error: this.mensaje}
        }
       
       }

    }


})
export default Reservas;

interface ErrorResponse {
    detail?: string; // La propiedad 'detail' contiene el mensaje de error, si está presente
  }
