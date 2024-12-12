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
                  <h2 class="mt-3 text-xl font-bold">{{Usuario[0].first_name }}</h2>
                  <p class="text-gray-500">{{  Usuario[0].email }}</p>
                </div>
                <el-descriptions class="mt-4" :column="1" border>
                  <el-descriptions-item label="Nombre">{{ Usuario[0].first_name}}</el-descriptions-item>
                  <el-descriptions-item label="Apellido">{{ Usuario[0].last_name
                    }}</el-descriptions-item>
                </el-descriptions>
                <div class="mt-4">
                  <el-button type="primary" @click="editProfile"
                    class="w-full bg-custom-green hover:bg-custom-green-dark">
                    Editar Perfil
                  </el-button>
                </div>
              </el-card>
            </el-col>
            <el-col :span="16">
              <el-card>
                <template #header>
                  <div class="flex justify-between items-center">
                    <span class="font-bold text-lg">Historial de mi usuario</span>
                    <el-button type="primary" class="bg-custom-green hover:bg-custom-green-dark">
                      Nueva Reserva
                    </el-button>
                  </div>
                </template>
                <el-table :data="reservations" style="width: 100%">
                  <el-table-column prop="date" label="Fecha" width="120">
                    <template #default="scope">
                      {{ formatDate(scope.row.date) }}
                    </template>
                  </el-table-column>
                  <el-table-column prop="court" label="Cancha" width="120" />
                  <el-table-column prop="time" label="Hora" width="120" />
                  <el-table-column prop="status" label="Estado">
                    <template #default="scope">
                      <el-tag :type="getStatusType(scope.row.status)">
                        {{ scope.row.status }}
                      </el-tag>
                    </template>
                  </el-table-column>
                  <el-table-column label="Acciones" width="120">
                    <template #default="scope">
                      <el-button v-if="scope.row.status === 'Pendiente'" type="danger" size="small"
                        @click="cancelReservation(scope.row)">
                        Cancelar
                      </el-button>
                    </template>
                  </el-table-column>
                </el-table>
              </el-card>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { UserFilled, Calendar, Setting } from '@element-plus/icons-vue'
import store from '@/stores/login';
const userauth = store()
import router from '@/router';
import type { Ref } from 'vue';
import type Iusers from '@/interfaces/IUsers';
const Usuario: Ref<Array<Iusers>> = ref([]);
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
    console.log(Usuario.value)  
  }
}

onMounted(async () => {
  await GetUser()
  console.log(Usuario.value)
})

const reservations = ref([
  { id: 1, date: new Date('2023-06-10'), court: 'Cancha A', time: '18:00 - 19:00', status: 'Completada' },
  { id: 2, date: new Date('2023-06-15'), court: 'Cancha B', time: '20:00 - 21:00', status: 'Pendiente' },
  { id: 3, date: new Date('2023-06-20'), court: 'Cancha C', time: '17:00 - 18:00', status: 'Cancelada' },
  { id: 4, date: new Date('2023-06-25'), court: 'Cancha A', time: '19:00 - 20:00', status: 'Pendiente' },
])

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' })
}

const getStatusType = (status) => {
  switch (status) {
    case 'Completada':
      return 'success'
    case 'Pendiente':
      return 'warning'
    case 'Cancelada':
      return 'danger'
    default:
      return 'info'
  }
}

const editProfile = () => {
  ElMessage.info('Funcionalidad de edición de perfil aún no implementada')
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
const cancelReservation = (reservation) => {
  ElMessage.success(`Reserva para ${formatDate(reservation.date)} cancelada`)
  reservation.status = 'Cancelada'
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