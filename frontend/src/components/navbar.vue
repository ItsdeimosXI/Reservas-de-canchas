<template>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
    >
      <el-menu-item index="0">
        <img
        style="width: 50px"
        src="@/assets/images/logo.svg"
        alt="Element logo"
      />
      </el-menu-item>
     
      <el-menu-item index="1">Inicio</el-menu-item>

      <el-menu-item index="2">Reservas de canchas</el-menu-item>
      <el-menu-item index="3">Sobre Nosotros</el-menu-item>
      <router-link :to="{name :  'login'} ">
      <el-menu-item index="4">Inicio de sesion</el-menu-item>
    </router-link>
    </el-menu>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue'
  
  const activeIndex = ref('1')
  const handleSelect = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
  }
  </script>
  
  <style>
  .el-menu--horizontal > .el-menu-item:nth-child(1) {
    margin-right: auto;
  }
  </style>