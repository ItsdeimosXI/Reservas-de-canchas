<template>
    <el-menu
      :default-active="activeIndex"
      background-color="black"
      text-color="white"
      mode="horizontal"
      :ellipsis="false"
      router
    >
      <el-menu-item>
        <img
        style="width: 50px"
        src="@/assets/images/logo.svg"
        alt="Element logo"
      />
      </el-menu-item>
      <el-menu-item index="/">Inicio</el-menu-item>

      <el-menu-item index="/reservas">Reservas de canchas</el-menu-item>
      <el-menu-item index="/about">Sobre Nosotros</el-menu-item>

      <el-menu-item index="/login">Inicio de sesion</el-menu-item>

    </el-menu>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue'
  
  const activeIndex = ref('1')
  </script>
  
  <style>
  .el-menu--horizontal > .el-menu-item:nth-child(1) {
    margin-right: auto;
  }
  router-link {
    all: unset;
  }
  </style>