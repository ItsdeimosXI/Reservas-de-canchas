<template>
    <div class="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
      <div class="relative py-3 sm:max-w-xl sm:mx-auto">
        <div
          class="absolute inset-0 bg-gradient-to-r from-custom-green to-custom-green-dark shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl">
        </div>
        <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
          <div class="max-w-md mx-auto">
            <div>
              <h1 class="text-2xl font-semibold text-center mb-6">Crear Nuevo lugar</h1>
            </div>
            <form @submit.prevent="crearlugar" class="space-y-6">
              <div>
                <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
                <el-input v-model="lugares.nombre" id="nombre" required />
              </div>
              <div class="flex items-center justify-between mt-6">
                <el-button @click="cancelarCreacion" type="info" plain>Cancelar</el-button>
                <el-button type="primary" native-type="submit" :loading="creando" class="bg-custom-green hover:bg-custom-green-dark">
                  Crear lugar
                </el-button>
              </div>
            </form>
          </div>        
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { ElMessage } from 'element-plus'
  import store from '@/stores/lugares'
  const lugarstore = store();
  const lugares = ref({
    nombre: '',
  })
  
  const creando = ref(false)

  const crearlugar = async () => {
    const response = await lugarstore.CreateLugar(lugares.value.nombre)
    if (response.success){
        ElMessage.success('lugar creado con éxito')
        resetForm()
  }else{
    ElMessage.error('No se pudo crear el lugar')
  }
}
  const cancelarCreacion = () => {
    ElMessage.info('Creación de lugar cancelada')
    resetForm() 
  }
  
  const resetForm = () => {
    lugares.value = {
      nombre: ''
    }
  }
  </script>
  
  <style scoped>
  :root {
    --color-custom-green: #70EB4A;
    --color-custom-green-dark: #5AC93B;
  }
  
  .bg-custom-green {
    background-color: var(--color-custom-green);
  }
  
  .hover\:bg-custom-green-dark:hover {
    background-color: var(--color-custom-green-dark);
  }
  
  .from-custom-green {
    --tw-gradient-from: var(--color-custom-green);
    --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to, rgba(112, 235, 74, 0));
  }
  
  .to-custom-green-dark {
    --tw-gradient-to: var(--color-custom-green-dark);
  }
  
  /* Estilos adicionales para Element Plus */
  :deep(.el-input__inner),
  :deep(.el-textarea__inner) {
    border-radius: 0.375rem;
  }
  
  :deep(.el-input-number) {
    width: 100%;
  }
  
  :deep(.el-select) {
    width: 100%;
  }
  
  :deep(.el-button--primary) {
    background-color: var(--color-custom-green);
    border-color: var(--color-custom-green);
  }
  
  :deep(.el-button--primary:hover, .el-button--primary:focus) {
    background-color: var(--color-custom-green-dark);
    border-color: var(--color-custom-green-dark);
  }
  </style>
  
  