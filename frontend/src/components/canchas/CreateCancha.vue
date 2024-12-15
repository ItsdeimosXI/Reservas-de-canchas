<template>
    <div class="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
      <div class="relative py-3 sm:max-w-xl sm:mx-auto">
        <div
          class="absolute inset-0 bg-gradient-to-r from-custom-green to-custom-green-dark shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl">
        </div>
        <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
          <div class="max-w-md mx-auto">
            <div>
              <h1 class="text-2xl font-semibold text-center mb-6">Crear Nueva Cancha</h1>
            </div>
            <form @submit.prevent="crearCancha" class="space-y-6">
              <div>
                <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
                <el-input v-model="cancha.nombre" id="nombre" required />
              </div>
              
              <div>
                <label for="numero_cancha" class="block text-sm font-medium text-gray-700">Número de Cancha</label>
                <el-input-number v-model="cancha.numero_cancha" :min="1" id="numero_cancha" required />
              </div>
              
              <div>
                <label for="descripcion" class="block text-sm font-medium text-gray-700">Descripción</label>
                <el-input v-model="cancha.descripcion" type="textarea" :rows="3" id="descripcion" required />
              </div>
              
              <div>
                <label for="tipo" class="block text-sm font-medium text-gray-700">Tipo</label>
                <el-select v-model="cancha.tipo" id="tipo" placeholder="Selecciona un tipo" required>
                  <el-option label="5v5" value="5v5" />
                  <el-option label="7v7" value="7v7" />
                  <el-option label="11v11" value="11v11" />
                </el-select>
              </div>
              
              <div>
                <label for="lugar" class="block text-sm font-medium text-gray-700">Lugar</label>
                <el-select 
                  v-model="cancha.lugar" 
                  id="lugar" 
                  placeholder="Selecciona un lugar" 
                  required
                  :loading="loadingLugares"
                >
                  <el-option
                    v-for="lugar in lugares"
                    :key="lugar.id"
                    :label="lugar.nombre"
                    :value="lugar.id"
                  />
                </el-select>
              </div>
              
              <div>
                <label for="precio" class="block text-sm font-medium text-gray-700">Precio por Hora</label>
                <el-input-number v-model="cancha.precio" :min="0" :precision="2" :step="10" id="precio" required />
              </div>
              
              <div class="flex items-center justify-between mt-6">
                <el-button @click="cancelarCreacion" type="info" plain>Cancelar</el-button>
                <el-button type="primary" native-type="submit" :loading="creando" class="bg-custom-green hover:bg-custom-green-dark">
                  Crear Cancha
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
  import storecanchas from '@/stores/reservas'
  const lugar = store();
  const canchastore = storecanchas();
  const cancha = ref({
    nombre: '',
    numero_cancha: 1,
    descripcion: '',
    tipo: '',
    lugar: '',
    precio: 0
  })
  
  const lugares = ref([])
  const loadingLugares = ref(false)
  const creando = ref(false)
  
  onMounted(async () => {
    await fetchLugares()
  })
  
  const fetchLugares = async () => {
    const response = await lugar.GetLugares()
    if (response.success){
        lugares.value = lugar.lugar
    }
    else{
        ElMessage.error('No se pudieron cargar los lugares')
    }
  }
  
  const crearCancha = async () => {
    const response = await canchastore.CrearCancha(cancha.value.nombre, cancha.value.numero_cancha, cancha.value.descripcion, cancha.value.tipo, cancha.value.lugar, cancha.value.precio)
    if (response.success){
        ElMessage.success('Cancha creada con éxito')
        resetForm()
  }else{
    ElMessage.error('No se pudo crear la cancha')
  }
}
  const cancelarCreacion = () => {
    ElMessage.info('Creación de cancha cancelada')
    resetForm() 
  }
  
  const resetForm = () => {
    cancha.value = {
      nombre: '',
      numero_cancha: 1,
      descripcion: '',
      tipo: '',
      lugar: '',
      precio: 0
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
  
  