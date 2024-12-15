<!-- src/components/NotFound.vue -->
<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-blue-50">
      <el-card class="max-w-md mx-auto p-8 bg-blue-100 shadow-lg">
        <h1 class="text-4xl font-bold text-blue-600 mb-4">404</h1>
        <p class="text-lg text-blue-500 mb-6">¡Oops! La página que buscas no existe.</p>
        <el-button type="primary" @click="goHome">Volver al inicio</el-button>
      </el-card>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  import { ElCard, ElButton } from 'element-plus';
  
  // Utilizamos `useRouter` para acceder a la instancia del enrutador
  const router = useRouter();
  
  // Función para redirigir al inicio
  const goHome = () => {
    router.push('/');
  };
  </script>
  
  <style scoped>
  /* Puedes agregar estilos personalizados aquí si es necesario */
  </style>
  