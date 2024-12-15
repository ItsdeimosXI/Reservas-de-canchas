<template>
  <div class="min-h-screen bg-gray-100">
    <el-container class="h-screen">
      <el-container>
        <el-header class="bg-white shadow">
          <div class="flex justify-between items-center h-full">
            <h2 class="text-xl font-semibold">Perfil de Usuario</h2>
            <el-button type="danger" @click="logout">Cerrar Sesión</el-button>
          </div>
        </el-header>

        <el-main>
          <el-row :gutter="20">
            <el-col :span="8">
              <el-card class="mb-4" v-if="Usuario.length > 0">
                <div>
                  <h2 class="mt-3 text-xl font-bold">{{ Usuario[0].username }}</h2>
                  <p class="text-gray-500">{{ Usuario[0].email }}</p>
                </div>
                <el-descriptions class="mt-4" :column="1" border>
                  <el-descriptions-item label="Nombre">{{ Usuario[0].first_name }}</el-descriptions-item>
                  <el-descriptions-item label="Apellido">{{ Usuario[0].last_name
                    }}</el-descriptions-item>
                </el-descriptions>
              </el-card>
            </el-col>
            <el-col :span="16">
              <el-card>
                <template #header>
                  <div class="flex justify-between items-center">
                    <span class="font-bold text-lg">Historial de mi usuario</span>
                    <el-button type="primary" class="bg-custom-green hover:bg-custom-green-dark" @click="router.push('/reservas/')">
                      Nueva Reserva
                    </el-button>
                  </div>
                </template>
                <div>
                  <div v-loading="loading" element-loading-text="Cargando canchas reservadas..." element-loading-background="rgba(0, 0, 0, 0.8)"
                  style="width: 100%" :data="OrdFecha">
                  <el-table :data="OrdFecha" style="width: 100%">
                    <el-table-column prop="dia" label="Fecha" width="120" sortable>
                    </el-table-column>
                    <el-table-column prop="nombre_cancha" label="Cancha" width="120" />
                    <el-table-column prop="horario_desde" label="Hora de comienzo" width="120" />
                    <el-table-column prop="horario_hasta" label="Hora de finalizacion" width="120" />
                    <el-table-column prop="status" label="Estado">
                      <template #default="scope">
                        <el-tag :type="getStatusType(scope.row.status)">
                          {{ scope.row.status }}
                        </el-tag>
                      </template>
                    </el-table-column>
                    <el-table-column label="Acciones" width="120">
                      <template #default="scope">
                        <el-button v-if="scope.row.status === 'pendiente'" type="danger" size="small"
                          @click="cancelReservation(scope.row.id, 'cancelada', scope.row.dia, scope.row.cancha_reservada, scope.row.horario_desde, scope.row.horario_hasta)">
                          Cancelar
                        </el-button>
                      </template>
                    </el-table-column>
                  </el-table>
                </div>
              </div>
              </el-card>

            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { computed, onMounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { UserFilled, Calendar, Setting } from '@element-plus/icons-vue'
import store from '@/stores/login';
const userauth = store()
import res from '@/stores/reservas';
const reservas = res()
import router from '@/router';
import type { Ref } from 'vue';
import type IReservas from '@/interfaces/IReservas';
import type Iusers from '@/interfaces/IUsers';
const Usuario: Ref<Array<Iusers>> = ref([]);
const loading = ref(true)
const GetUser = async () => {
  const response = await userauth.GetUser()
  if (!response.success) {
    ElMessage({
      showClose: true,
      duration: 5 * 1000,
      type: 'error',
      message: 'Error al ver su usuario intente nuevamente mas tarde',
    })

  } else if (userauth.user) {
    Usuario.value = userauth.user
    
  }
}

onMounted(async () => {
  await GetUser()
  
  await GetReservaciones()

})
const reservations: Ref<Array<IReservas>> = ref([])
const GetReservaciones = async () => {
  const response = await reservas.GetReservas()
  if (!response.success) {
    ElMessage({
      showClose: true,
      duration: 5 * 1000,
      type: 'error',
      message: 'Error al ver sus reservas intente nuevamente mas tarde',
    })
  } else if (reservas.reservas_user) {
    reservations.value = reservas.reservas_user
    loading.value = false
  }
}
const OrdFecha= computed(() =>
  [...reservations.value].sort((a, b) => new Date(a.dia).getTime() - new Date(b.dia).getTime())
);
const getStatusType = (status: any) => {
  switch (status) {
    case 'completada':
      return 'success'
    case 'pendiente':
      return 'warning'
    case 'cancelada':
      return 'danger'
    default:
      return 'info'
  }
}

const logout = () => {
  const response = userauth.logout()
  if (!response.success) {
    ElMessage({
      showClose: true,
      duration: 5 * 1000,
      type: 'error',
      message: 'Error al cerrar sesion intente nuevamente mas tarde',
    })
  } else {
    ElMessage({
      showClose: true,
      duration: 5 * 1000,
      type: 'success',
      message: 'Sesion cerrada exitosamente',
    })
    router.push('/')
  }
}
const cancelReservation = async (id: number, status = 'cancelada', dia: string, cancha_reservada: string, horario_desde: string, horario_hasta: string) => {
  const response = await reservas.CancelarReserva(id, status, dia, cancha_reservada, horario_desde, horario_hasta)
  if (response.success) {
    ElMessage.success(`Su reserva ha sido cancelada`)
    GetReservaciones()
  }
  else {
    ElMessage.error(`Error al cancelar su reserva intente de nuevo mas tarde`)
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

.text-custom-green {
  color: var(--color-custom-green);
}

.hover\:bg-custom-green-dark:hover {
  background-color: var(--color-custom-green-dark);
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

:deep(.el-menu-item.is-active) {
  background-color: #374151 !important;
}

:deep(.el-table) {
  --el-table-border-color: #e5e7eb;
  --el-table-header-background-color: #f3f4f6;
}

:deep(.el-table th) {
  background-color: #f3f4f6;
}

:deep(.el-card) {
  border-radius: 0.5rem;
}

:deep(.el-card__header) {
  padding: 1rem;
  border-bottom: 1px solid #e5e7eb;
}
</style>