<template>
    <el-menu
      :default-active="activeIndex"
      background-color="black"
      text-color="white"
      mode="horizontal"
      :ellipsis="false"
    >
      <el-menu-item index="0">
        <router-link :to="{name :  'home'} ">
        <img
        style="width: 50px"
        src="@/assets/images/logo.svg"
        alt="Element logo"
      />
    </router-link>
      </el-menu-item>
     <router-link :to="{name :  'home'} ">
      <el-menu-item index="1">Inicio</el-menu-item>
    </router-link>
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
  router-link {
    text-decoration: none;
  }
  </style>