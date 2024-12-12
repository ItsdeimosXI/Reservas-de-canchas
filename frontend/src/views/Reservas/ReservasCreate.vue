  <template>
    <div class="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
      <div class="relative py-3 sm:max-w-xl sm:mx-auto">
        <div
          class="absolute inset-0 bg-gradient-to-r from-custom-green to-custom-green-dark shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl">
        </div>
        <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
          <div class="max-w-md mx-auto">
            <div>
              <h1 class="text-2xl font-semibold text-center">Crear Reserva de Cancha</h1>
            </div>
            <div class="divide-y divide-gray-200">
              <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                <div class="flex flex-col">
                  <label class="leading-loose">Fecha de Reserva</label>
                  <el-date-picker v-model="fechaReserva" type="date" placeholder="Selecciona una fecha"
                    :disabled-date="disabledDate" @change="actualizarHorariosDisponibles" value-format="YYYY-MM-DD" />
                </div>
                <div class="flex flex-col">
                  <label class="leading-loose">Hora de Inicio</label>
                  <el-time-select v-model="horaInicio" :max-time="horaFin" class="mr-4" :disabled="!fechaReserva"
                    :editable="false" :clearable="false" start="08:00" step="01:00" end="22:00"
                    placeholder="Hora de inicio" @change="calcularPrecio" />
                </div>
                <div class="flex flex-col">
                  <label class="leading-loose">Hora de Fin</label>
                  <el-time-select v-model="horaFin" :min-time="horaInicio" :disabled="!horaInicio" :editable="false"
                    :clearable="false" start="09:00" step="01:00" end="23:00" placeholder="Hora de fin"
                    @change="calcularPrecio" />
                </div>
                <div v-loading="loading" element-loading-text="Cargando cancha..."
                  element-loading-background="rgba(0, 0, 0, 0.8)" style="width: 100%">
                  <div class="bg-white overflow-hidden shadow-sm rounded-lg">
                    <div class="p-6">
                      <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ nombreCancha }}</h3>
                      <p class="text-gray-600 mb-2">Lugar: {{ LugarCancha }}</p>
                      <p class="text-gray-600 mb-2">Tipo: {{ TipoCancha }}</p>
                      <p class="text-gray-600 mb-4">Descripcion: {{ DescripcionCancha }}</p>
                    </div>
                  </div>
                  <div v-if="precioTotal > 0" class="flex items-center justify-between">
                    <span class="text-lg font-semibold">Precio Total:</span>
                    <span class="text-2xl font-bold text-custom-green">${{ precioTotal.toFixed(2) }}</span>
                  </div>
                </div>
                <div class="pt-4 flex items-center space-x-4">
                  <button @click="cancelarReserva"
                    class="flex justify-center items-center w-full text-gray-900 px-4 py-3 rounded-md focus:outline-none">
                    <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12">
                      </path>
                    </svg> Cancelar
                  </button>
                  <button @click="crearReserva"
                    class="bg-custom-green flex justify-center items-center w-full text-white px-4 py-3 rounded-md focus:outline-none">Crear
                    Reserva</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { useRoute } from 'vue-router';
import router from '@/router';
import Reservas from '@/stores/reservas';
const loading = ref(true)
const reservas = Reservas();
const fechaReserva = ref('')
const horaInicio = ref('')
const horaFin = ref('')
const precioTotal = ref(0)
const route = useRoute();
const canchaId = route.params.id;
const nombreCancha = ref('')
const LugarCancha = ref('')
const TipoCancha = ref('')
const DescripcionCancha = ref('')
const precio = ref('')
const disabledDate = (time) => {
  return time.getTime() < Date.now() - 8.64e7; // Deshabilita fechas anteriores a hoy
}
const GetCanchas = async () => {
  const response = await reservas.GetCanchasByID(canchaId)
  if (!response.success) {
    ElMessage({
      showClose: true,
      duration: 5 * 1000,
      type: 'error',
      message: 'Error al obtener la cancha, intente mas tarde',
    })
  } else if (reservas.canchas) {
    nombreCancha.value = reservas.canchas.nombre
    LugarCancha.value = reservas.canchas.lug
    TipoCancha.value = reservas.canchas.tipo
    DescripcionCancha.value = reservas.canchas.descripcion
    precio.value = reservas.canchas.precio
    loading.value = false
  }
}
onMounted(async () => {
  await GetCanchas()
})
const actualizarHorariosDisponibles = () => {
  // Aquí se podría implementar la lógica para actualizar los horarios disponibles
  // basándose en las reservas existentes para la fecha seleccionada
  console.log("Actualizando horarios disponibles para:", fechaReserva.value)
}

const calcularPrecio = () => {
  if (horaInicio.value && horaFin.value && precio.value) {
    const inicio = new Date(`2000-01-01T${horaInicio.value}`)
    const fin = new Date(`2000-01-01T${horaFin.value}`)
    const duracionHoras = (fin - inicio) / 3600000
    const precioxhora = parseFloat(precio.value)
    precioTotal.value = duracionHoras * precioxhora
  } else {
    precioTotal.value = 0
  }
}

const crearReserva = async () => {
  if (!fechaReserva.value || !horaInicio.value || !horaFin.value) {
    ElMessage.error('Por favor, completa todos los campos')
    return
  }
  const response = await reservas.CreateReserva(
    canchaId,
    horaInicio.value,
    horaFin.value,
    fechaReserva.value
  )
  if (!response.success) {
    ElMessage({
      showClose: true,
      duration: 5 * 1000,
      type: 'error',
      message: 'Error al crear la reserva intente de nuevo mas tarde',
    })
  } else{
    ElMessage({
      showClose: true,
      duration: 5 * 1000,
      type: 'success',
      message: 'Reserva creada con exito',
    })
    router.push('/reservas')
  }
}

const cancelarReserva = () => {
  // Reiniciar todos los campos
  fechaReserva.value = ''
  horaInicio.value = ''
  horaFin.value = ''
  precioTotal.value = 0

  ElMessage.info('Reserva cancelada')
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

.text-custom-green {
  color: var(--color-custom-green);
}

.from-custom-green {
  --tw-gradient-from: var(--color-custom-green);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to, rgba(112, 235, 74, 0));
}

.to-custom-green-dark {
  --tw-gradient-to: var(--color-custom-green-dark);
}

/* Estilos adicionales para Element Plus */
:deep(.el-input__inner) {
  border-radius: 0.375rem;
}

:deep(.el-select .el-input__inner) {
  border-radius: 0.375rem;
}

:deep(.el-date-editor.el-input),
:deep(.el-date-editor.el-input__inner) {
  width: 100%;
}
</style>

