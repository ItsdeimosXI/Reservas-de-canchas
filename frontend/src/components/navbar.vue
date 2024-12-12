<template>
  <el-menu :default-active="activeIndex" background-color="black" text-color="white" mode="horizontal" :ellipsis="false"
    router>
    <el-menu-item>
      <img style="width: 50px" src="@/assets/images/logo.svg" alt="Element logo" />
    </el-menu-item>
    <el-menu-item index="/">Inicio</el-menu-item>

    <el-menu-item index="/reservas">Reservas de canchas</el-menu-item>
    <el-menu-item index="/about">Sobre Nosotros</el-menu-item>

    <el-menu-item v-if="!IsAuth" index="/login">Inicio de sesion</el-menu-item>
    <el-sub-menu v-if="IsAuth" index="user">
      <template #title>
      <el-avatar
        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
      />
      </template>
    <el-menu-item index="/perfil">Perfil</el-menu-item>
    <el-menu-item  @click="logout">Cerrar sesion</el-menu-item>
  </el-sub-menu>
  </el-menu>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'
import store from '@/stores/login';
import router from '@/router';
import { ElMessage } from 'element-plus';
const activeIndex = ref('1')
const userauth = store()
const IsAuth = computed(() => !!userauth.token)
const logout = () => {
  const response = userauth.logout()
  if (!response.success){
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

</script>

<style>
.el-menu--horizontal>.el-menu-item:nth-child(1) {
  margin-right: auto;
}

router-link {
  all: unset;
}
</style>