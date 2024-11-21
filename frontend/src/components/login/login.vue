<template>
<div class="min-h-screen flex items-center justify-center bg-gray-100">
  <div class="bg-white p-6 rounded shadow-md w-full max-w-sm">
    <h2 class="text-2xl font-bold text-gray-700 text-center mb-6">Iniciar Sesión</h2>
    <div class="mb-4">
    <label class="block text-gray-700 font-bold mb-2">Nombre de usuario</label>
    <input class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" type="text" placeholder="Username" v-model="username">
  </div>
  <div class="mb-6">
    <label class="block text-gray-700 font-bold mb-2">Contraseña</label>
    <input type="text" placeholder="Contraseña" class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500" v-model="password">
  </div>
  <div class="mb-6 flex items-center">
    <el-switch
    v-model="rememberMe"
    class="ml-2"
    style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
  />
      <label for="remember_me" class="ml-2 text-sm text-gray-700" >Recordar sesión?</label>
    </div>
    <button class="px-5 py-3 bg-blue-500 text-black rounded hover:bg-blue-800" @click="login">Enviar</button>
  </div>
</div>
</template>
<script lang="ts" setup>
import store from '@/stores/login';
import { ref } from 'vue';
import { ElMessage } from 'element-plus'
import type { Ref } from 'vue';
const username:Ref<string> = ref('');
const password:Ref<string> = ref('');
const rememberMe:Ref<boolean> = ref(false);
const AuthUser = store();
  const login = async () => {
   const response = await AuthUser.login(username.value, password.value, rememberMe.value);
    if (AuthUser.errores !== null){
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
    }
    console.log(AuthUser.errores)
  }
</script>
<style scoped>

</style>