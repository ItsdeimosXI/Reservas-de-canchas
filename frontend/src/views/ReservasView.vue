<template>
  <div v-loading="loading" element-loading-text="Cargando canchas..." element-loading-background="rgba(0, 0, 0, 0.8)"
    style="width: 100%" :data="canchas">
    <div class="min-h-screen bg-gray-100">

      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-900 mb-6">Reserva de Canchas</h1>

        <!-- Filtro por lugar -->
        <div class="mb-6">
          <label for="lugar" class="block text-sm font-medium text-gray-700">Filtrar por lugar:</label>
          <select id="lugar" v-model="lugarSeleccionado" @change="filtrarCanchas"
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-custom-green focus:border-custom-green sm:text-sm rounded-md">
            <option value="">Todos los lugares</option>
            <option v-for="lugar in lugares" :key="lugar" :value="lugar">
              {{ lugar }}
            </option>
          </select>
        </div>
        <!-- Lista de canchas -->
        <div v-if="canchasFiltradas.length > 0" class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <div v-for="cancha in canchasFiltradas" :key="cancha.id"
            class="bg-white overflow-hidden shadow-sm rounded-lg">
            <div class="p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ cancha.nombre }}</h3>
              <p class="text-gray-600 mb-2">Lugar: {{ cancha.lug }}</p>
              <p class="text-gray-600 mb-2">Tipo: {{ cancha.tipo }}</p>
              <p class="text-gray-600 mb-2">precio: {{ cancha.precio }}</p>
              <p class="text-gray-600 mb-4">Descripcion: {{ cancha.descripcion }}</p>
              <router-link :to="{ path: '/reservas/crear/' + cancha.id }">
                <button
                  class="w-full bg-custom-green text-black font-semibold py-2 px-4 rounded-md hover:bg-custom-green-dark transition duration-300">

                  Reservar

                </button>
              </router-link>
            </div>
          </div>
        </div>
        <div v-else class="text-center text-gray-600 mt-8">
          No se encontraron canchas disponibles para el lugar seleccionado.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, type Ref } from 'vue'
import Reservas from '@/stores/reservas';
import { ElMessage } from 'element-plus';
import type ICanchas from '@/interfaces/ICanchas';
const reservas = Reservas();
const loading = ref(true)
const fetchCanchas = async () => {

  const response = await reservas.GetCanchas()
  if (!response.success) {
    ElMessage({
      showClose: true,
      duration: 5 * 1000,
      type: 'error',
      message: 'Error al ver las canchas intente nuevamente mas tarde',
    })

  } else if (reservas.canchas) {
    canchas.value = reservas.canchas
    loading.value = false
  }
}
import store from '@/stores/login';
const userauth = store()
const canchas: Ref<Array<ICanchas>> = ref([]);
const lugarSeleccionado = ref('');
const lugares: Ref<Array<string>> = ref([]);
const IsAuth = computed(() => !!userauth.token)
const ObtenerUsuario = async () => {
  const response = await userauth.GetUser();
};
onMounted(async () => {
  await fetchCanchas();
  lugares.value = [...new Set(canchas.value.map(cancha => cancha.lug))];
  if(userauth.token){
    await ObtenerUsuario()
  }
});

const canchasFiltradas = computed(() => {
  if (lugarSeleccionado.value) {
    return canchas.value.filter(cancha => cancha.lug === lugarSeleccionado.value)
  }
  return canchas.value
})

const filtrarCanchas = () => {
  // Esta función se llama cuando cambia el filtro, pero no necesita hacer nada adicional
  // ya que el cómputo de canchasFiltradas se actualiza automáticamente
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

.focus\:ring-custom-green:focus {
  --tw-ring-color: var(--color-custom-green);
}

.focus\:border-custom-green:focus {
  border-color: var(--color-custom-green);
}
</style>