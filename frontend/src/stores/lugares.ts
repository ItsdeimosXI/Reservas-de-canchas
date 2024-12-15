// Importación de dependencias necesarias
import { defineStore } from 'pinia';
import axios, { AxiosError } from 'axios'; 

const Lugares = defineStore('Lugares', {
    state: () => {
        return {
            mensaje: '' as string | null,
            lugar: null as Array<any> | null,
            errores: null as number | null,
        }
    },
    actions: {
        async GetLugares(){
            try{
            const response = await axios.get('/api/lugar/')
            this.lugar = response.data.results
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
export default Lugares;

interface ErrorResponse {
    detail?: string; // La propiedad 'detail' contiene el mensaje de error, si está presente
    }