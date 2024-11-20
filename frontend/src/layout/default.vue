<template>
    <div>
      <navbar />
      <main>
        <slot></slot>
      </main>
      <AppFooter />
    </div>
  </template>
  
  <script setup lang="ts">
  import navbar from '@/components/navbar.vue';
  import AppFooter from '@/components/AppFooter.vue';
  </script>
  
  <style scoped>
  /* Puedes agregar estilos específicos aquí si es necesario */
  </style>
  