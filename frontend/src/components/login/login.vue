<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Iniciar sesión en RAPITURNO
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          ¿No tienes una cuenta?
          <router-link :to="{ name: 'register'}" class="font-medium text-custom-green hover:text-custom-green-dark">
            Regístrate aquí
          </router-link>
        </p>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="login">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username-address" class="sr-only">Correo electrónico</label>
            <input id="username-address" name="username" type="username" autocomplete="username" required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-custom-green focus:border-custom-green focus:z-10 sm:text-sm"
              placeholder="Nombre de usuario" v-model="username" />
          </div>
          <div>
            <label for="password" class="sr-only">Contraseña</label>
            <input id="password" name="password" type="password" autocomplete="current-password" required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-custom-green focus:border-custom-green focus:z-10 sm:text-sm"
              placeholder="Contraseña" v-model="password" />
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input id="remember-me" name="remember-me" type="checkbox"
              class="h-4 w-4 text-custom-green focus:ring-custom-green border-gray-300 rounded" v-model="rememberMe" />
            <label for="remember-me" class="ml-2 block text-sm text-gray-900">
              Recordarme
            </label>
          </div>
        </div>

        <div>
          <button type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-black bg-custom-green hover:bg-custom-green-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-custom-green">
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <LockClosedIcon class="h-5 w-5 text-custom-green-dark group-hover:text-custom-green-light" aria-hidden="true" />
            </span>
            Iniciar sesión
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
<script lang="ts" setup>
import store from '@/stores/login';
import { ref } from 'vue';
import { ElMessage } from 'element-plus'
import type { Ref } from 'vue';
import router from '@/router';
const username:Ref<string> = ref('');
const password:Ref<string> = ref('');
const rememberMe:Ref<boolean> = ref(false);
const AuthUser = store();
  const login = async () => {
   const response = await AuthUser.login(username.value, password.value, rememberMe.value);
    if (!response.success){
      ElMessage({
        showClose: true,
        duration: 5 * 1000,
          type: 'error',
          message: 'Error al iniciar sesion / contraseña o usuario incorrecto',
        })
    } else {
      ElMessage ({
        type: 'success',
        message: 'Inicio de sesion correcto',
      })
      router.push('/reservas')
    }
    console.log(AuthUser.errores)
  }
</script>
<style scoped>

</style>