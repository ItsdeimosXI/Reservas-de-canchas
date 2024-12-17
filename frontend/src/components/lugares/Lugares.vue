<template>
    <div class="min-h-screen bg-gray-100 py-6 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <h1 class="text-3xl font-bold text-gray-900 mb-6">Gestión de Lugar</h1>
        
        <el-button type="primary" class="mb-6 bg-custom-green hover:bg-custom-green-dark" @click="navigateToCrearLugar">
          Crear Nueva Lugar
        </el-button>
        <el-table
          v-loading="loading"
          :data="lugares"
          style="width: 100%"
          :row-class-name="tableRowClassName"
        >
          <el-table-column prop="nombre" label="Nombre" />
          <el-table-column label="Acciones" width="200">
            <template #default="scope">
              <el-button
                size="small"
                type="primary"
                @click="modificarLugar(scope.row)"
                class="mr-2 bg-custom-green hover:bg-custom-green-dark"
              >
                Modificar
              </el-button>
              <el-button
                size="small"
                type="danger"
                @click="confirmarEliminarLugar(scope.row)"
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
        title="Modificar Lugar"
        width="50%"
        :before-close="handleClose"
      >
        <el-form :model="LugarSeleccionado" label-width="120px">
          <el-form-item label="Nombre">
            <el-input v-model="LugarSeleccionado.nombre" />
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
  import router from '@/router';
  const storelugar = Lugares()
  const loading = ref(true)
  const dialogVisible = ref(false)
  const LugarSeleccionado = ref({})
  const lugares = ref([])
  
  onMounted(async () => {
    await fetchLugares()
  })
  
  const fetchLugares = async () => {
    const response = await storelugar.GetLugares()
    if (response.success){
        lugares.value = storelugar.lugar
        loading.value = false
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
  
  const modificarLugar = (Lugar) => {
    LugarSeleccionado.value = { ...Lugar }
    dialogVisible.value = true
  }
  
  const guardarModificacion = async () => {
    const response = await storelugar.ModificarLugar(LugarSeleccionado.value.id,LugarSeleccionado.value.nombre)
    if (response.success){
        ElMessage.success('Lugar modificada con éxito')
        await fetchLugares()
        dialogVisible.value = false
    }
    else{
        ElMessage.error('No se pudo modificar la Lugar')
    }
  }
  
  const confirmarEliminarLugar = (Lugar) => {
    ElMessageBox.confirm(
      `¿Estás seguro de que quieres eliminar la Lugar "${Lugar.nombre}"?`,
      'Advertencia',
      {
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar',
        type: 'warning',
      }
    )
      .then(() => {
        eliminarLugar(Lugar)
      })
      .catch(() => {
        ElMessage.info('Eliminación cancelada')
      })
  }
  
  const eliminarLugar = async (Lugar) => {
    const response = await storelugar.EliminarLugar(Lugar.id)
    if (response.success){
        ElMessage.success('Lugar eliminada con éxito')
        await fetchLugares()
    }
    else{
        ElMessage.error('No se pudo eliminar la Lugar')
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
  
  const navigateToCrearLugar = () => {
    router.push('/crearlugar')
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
  
  