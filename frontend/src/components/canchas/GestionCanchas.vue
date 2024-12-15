<template>
    <div class="min-h-screen bg-gray-100 py-6 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <h1 class="text-3xl font-bold text-gray-900 mb-6">Gestión de Canchas</h1>
        
        <el-button type="primary" class="mb-6 bg-custom-green hover:bg-custom-green-dark" @click="navigateToCrearCancha">
          Crear Nueva Cancha
        </el-button>
  
        <el-table
          v-loading="loading"
          :data="canchas"
          style="width: 100%"
          :row-class-name="tableRowClassName"
        >
          <el-table-column prop="nombre" label="Nombre" />
          <el-table-column prop="numero_cancha" label="Número" width="100" />
          <el-table-column prop="tipo" label="Tipo" width="100" />
          <el-table-column prop="lug" label="Lugar" />
          <el-table-column prop="precio" label="Precio/Hora" width="120">
            <template #default="scope">
              ${{ scope.row.precio.toFixed(2) }}
            </template>
          </el-table-column>
          <el-table-column label="Acciones" width="200">
            <template #default="scope">
              <el-button
                size="small"
                type="primary"
                @click="modificarCancha(scope.row)"
                class="mr-2 bg-custom-green hover:bg-custom-green-dark"
              >
                Modificar
              </el-button>
              <el-button
                size="small"
                type="danger"
                @click="confirmarEliminarCancha(scope.row)"
              >
                Eliminar
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
  
      <!-- Modal de Modificación -->
      <el-dialog
        v-model="dialogVisible"
        title="Modificar Cancha"
        width="50%"
        :before-close="handleClose"
      >
        <el-form :model="canchaSeleccionada" label-width="120px">
          <el-form-item label="Nombre">
            <el-input v-model="canchaSeleccionada.nombre" />
          </el-form-item>
          <el-form-item label="Número">
            <el-input-number v-model="canchaSeleccionada.numero_cancha" :min="1" />
          </el-form-item>
          <el-form-item label="Descripción">
            <el-input v-model="canchaSeleccionada.descripcion" type="textarea" />
          </el-form-item>
          <el-form-item label="Tipo">
            <el-select v-model="canchaSeleccionada.tipo">
              <el-option label="5v5" value="5v5" />
              <el-option label="7v7" value="7v7" />
              <el-option label="11v11" value="11v11" />
            </el-select>
          </el-form-item>
          <el-form-item label="Lugar">
            <el-select v-model="canchaSeleccionada.lugar">
              <el-option
                v-for="lugar in lugares"
                :key="lugar.id"
                :label="lugar.nombre"
                :value="lugar.id"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="Precio por Hora">
            <el-input-number v-model="canchaSeleccionada.precio" :min="0" :precision="2" :step="10" />
          </el-form-item>
        </el-form>
        <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible = false">Cancelar</el-button>
            <el-button type="primary" @click="guardarModificacion" class="bg-custom-green hover:bg-custom-green-dark">
              Guardar
            </el-button>
          </span>
        </template>
      </el-dialog>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  import Lugares from '@/stores/lugares';
  import Reservas from '@/stores/reservas';
  import router from '@/router';
  const storelugar = Lugares()
  const storereservas =  Reservas()
  const canchas = ref([])
  const loading = ref(true)
  const dialogVisible = ref(false)
  const canchaSeleccionada = ref({})
  const lugares = ref([])
  
  onMounted(async () => {
    await fetchCanchas()
    await fetchLugares()
  })
  
  const fetchCanchas = async () => {
    loading.value = true
    const response = await storereservas.GetCanchas()
    if (response.success){
        canchas.value = storereservas.canchas
    }
    else{
        ElMessage.error('No se pudieron cargar las canchas')
    }
    loading.value = false
  }
  
  const fetchLugares = async () => {
    const response = await storelugar.GetLugares()
    if (response.success){
        lugares.value = storelugar.lugar
    }
    else{
        ElMessage.error('No se pudieron cargar los lugares')
    }
  }
  
  const tableRowClassName = ({ row, rowIndex }) => {
    if (rowIndex % 2 === 0) {
      return 'bg-gray-50'
    }
    return ''
  }
  
  const modificarCancha = (cancha) => {
    canchaSeleccionada.value = { ...cancha }
    dialogVisible.value = true
  }
  
  const guardarModificacion = async () => {
    const response = await storereservas.ModificarCancha(canchaSeleccionada.value.id,canchaSeleccionada.value.nombre, canchaSeleccionada.value.numero_cancha, canchaSeleccionada.value.descripcion, canchaSeleccionada.value.tipo, canchaSeleccionada.value.lugar, canchaSeleccionada.value.precio)
    if (response.success){
        ElMessage.success('Cancha modificada con éxito')
        await fetchCanchas()
        dialogVisible.value = false
    }
    else{
        ElMessage.error('No se pudo modificar la cancha')
    }
  }
  
  const confirmarEliminarCancha = (cancha) => {
    ElMessageBox.confirm(
      `¿Estás seguro de que quieres eliminar la cancha "${cancha.nombre}"?`,
      'Advertencia',
      {
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar',
        type: 'warning',
      }
    )
      .then(() => {
        eliminarCancha(cancha)
      })
      .catch(() => {
        ElMessage.info('Eliminación cancelada')
      })
  }
  
  const eliminarCancha = async (cancha) => {
    const response = await storereservas.EliminarCancha(cancha.id)
    if (response.success){
        ElMessage.success('Cancha eliminada con éxito')
        await fetchCanchas()
    }
    else{
        ElMessage.error('No se pudo eliminar la cancha')
    }
  }
  const handleClose = (done) => {
    ElMessageBox.confirm('¿Estás seguro de cerrar sin guardar los cambios?')
      .then(() => {
        done()
      })
      .catch(() => {
        // Mantener el diálogo abierto
      })
  }
  
  const navigateToCrearCancha = () => {
    router.push('/canchascrear')
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
  
  /* Estilos adicionales para Element Plus */
  :deep(.el-table .el-table__cell) {
    padding: 12px 0;
  }
  
  :deep(.el-button--primary) {
    background-color: var(--color-custom-green);
    border-color: var(--color-custom-green);
  }
  
  :deep(.el-button--primary:hover, .el-button--primary:focus) {
    background-color: var(--color-custom-green-dark);
    border-color: var(--color-custom-green-dark);
  }
  
  :deep(.el-dialog__body) {
    padding-top: 20px;
  }
  </style>
  
  