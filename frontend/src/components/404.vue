<template>
  <div class="min-h-screen bg-gray-100 flex flex-col justify-center items-center px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 text-center">
      <div>
        <el-icon class="text-custom-green mx-auto h-24 w-24"><SoccerBall /></el-icon>
        <h2 class="mt-6 text-4xl font-extrabold text-gray-900">
          ¡Ups! Fuera de juego
        </h2>
        <p class="mt-2 text-lg text-gray-600">
          Parece que esta página se ha ido a entrenar. No la encontramos en la cancha.
        </p>
      </div>
      <div class="mt-8 space-y-4">
        <p class="text-sm text-gray-500">
          Error 404 - Página no encontrada
        </p>
        <el-button type="primary" class="w-full bg-custom-green hover:bg-custom-green-dark" @click="goHome">
          Volver al inicio
        </el-button>
        <el-button type="info" plain class="w-full" @click="goBack">
          Regresar a la página anterior
        </el-button>
      </div>
      <div class="mt-8">
        <p class="text-base text-gray-500">
          ¿Necesitas ayuda para encontrar lo que buscas?
        </p>
        <el-button type="text" class="text-custom-green hover:text-custom-green-dark" @click="contactSupport">
          Contacta con nuestro equipo de soporte
        </el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goHome = () => {
  router.push('/')
}

const goBack = () => {
  router.go(-1)
}

const contactSupport = () => {
  // Aquí puedes implementar la lógica para contactar al soporte
  // Por ejemplo, abrir un modal de contacto o navegar a una página de soporte
  console.log('Contactando al soporte...')
}
</script>

<style scoped>
:root {
  --color-custom-green: #70EB4A;
  --color-custom-green-dark: #5AC93B;
}

.text-custom-green {
  color: var(--color-custom-green);
}

.bg-custom-green {
  background-color: var(--color-custom-green);
}

.hover\:bg-custom-green-dark:hover {
  background-color: var(--color-custom-green-dark);
}

.hover\:text-custom-green-dark:hover {
  color: var(--color-custom-green-dark);
}

/* Estilos adicionales para Element Plus */
:deep(.el-button--primary) {
  background-color: var(--color-custom-green);
  border-color: var(--color-custom-green);
}

:deep(.el-button--primary:hover, .el-button--primary:focus) {
  background-color: var(--color-custom-green-dark);
  border-color: var(--color-custom-green-dark);
}

:deep(.el-button--text) {
  color: var(--color-custom-green);
}

:deep(.el-button--text:hover, .el-button--text:focus) {
  color: var(--color-custom-green-dark);
}
</style>

