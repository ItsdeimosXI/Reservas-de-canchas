<template>
    <footer class="bg-green-500 no-aos">
      <!-- Sección de íconos -->
      <div class="px-4 py-6 bg-green-700 text-center">
        <div class="flex justify-center gap-6">
          <a
            href="https://github.com/ItsdeimosXI"
            target="_blank"
            class="text-black text-4xl hover:text-white transition-colors"
            aria-label="GitHub"
          >
            <i class="fa-brands fa-github"></i>
          </a>
          <a
            href="https://www.linkedin.com/in/manuel-salamanca/"
            target="_blank"
            class="text-black text-4xl hover:text-white transition-colors"
            aria-label="LinkedIn"
          >
            <i class="fa-brands fa-linkedin"></i>
          </a>
        </div>
      </div>
  
      <!-- Sección de créditos -->
      <div class="px-4 py-6 bg-green-700 text-center">
        <span class="text-sm text-white">
          Diseño y desarrollo por 
          <a
            href="https://www.linkedin.com/in/manuel-salamanca/"
            class="hover:underline"
            target="_blank"
          >
            Manuel Salamanca
          </a>.
        </span>
      </div>
    </footer>
  </template>
  
  <script setup lang="ts"></script>
  
  <style scoped>
  .no-aos [data-aos] {
    transition: none !important;
    transform: none !important;
    opacity: 1 !important;
  }
  
  footer {
    position: relative;
    overflow-x: hidden;
  }
  </style>
  