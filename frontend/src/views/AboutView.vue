<template>
  <div class="min-h-screen bg-gray-100">
    <main class="py-16 px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <h1 class="text-4xl font-extrabold text-gray-900 text-center mb-8">
          Sobre RAPITURNO
        </h1>

        <section class="bg-white shadow-lg rounded-lg overflow-hidden mb-12">
          <div class="p-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Nuestra Misión</h2>
            <p class="text-gray-700 mb-6">
              En RAPITURNO, nuestra misión es simplificar la reserva de canchas deportivas,
              conectando a los amantes del deporte con los mejores espacios para jugar.
              Creemos en el poder del deporte para unir a las personas y promover un estilo
              de vida saludable.
            </p>
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Nuestra Historia</h2>
            <p class="text-gray-700 mb-6">
              Fundada en 2023, RAPITURNO nació de la frustración de un grupo de amigos
              que siempre luchaban para encontrar y reservar canchas para sus partidos semanales.
              Decidimos crear una solución que hiciera este proceso fácil y rápido para todos.
            </p>
          </div>
        </section>

        <section class="bg-white shadow-lg rounded-lg overflow-hidden mb-12">
          <div class="p-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-6">Lo Que Ofrecemos</h2>
            <ul class="space-y-4">
              <li class="flex items-start">
                <svg class="h-6 w-6 text-custom-green mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                <span class="text-gray-700">Reservas fáciles y rápidas de canchas deportivas</span>
              </li>
              <li class="flex items-start">
                <svg class="h-6 w-6 text-custom-green mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                <span class="text-gray-700">Amplia variedad de canchas: 5v5, 7v7, 11v11 y más</span>
              </li>
              <li class="flex items-start">
                <svg class="h-6 w-6 text-custom-green mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                <span class="text-gray-700">Múltiples ubicaciones en toda la ciudad</span>
              </li>
              <li class="flex items-start">
                <svg class="h-6 w-6 text-custom-green mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                <span class="text-gray-700">Sistema de gestión de turnos personalizado</span>
              </li>
            </ul>
          </div>
        </section>

        <section class="bg-white shadow-lg rounded-lg overflow-hidden">
          <div class="p-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-6 text-center">Desarrollado por</h2>
            <div class="grid grid-cols-1 md:grid-cols-1 gap-8">
              <div class="text-center">
                <div class="w-32 h-32 bg-gray-300 rounded-full mx-auto mb-4"></div>
                <h3 class="text-lg font-semibold text-gray-900">Manuel Salamanca</h3>
                <p class="text-gray-600">Desarollador web</p>
              </div>
            </div>
          </div>
        </section>
        <section class="bg-white shadow-lg rounded-lg overflow-hidden mb-12 text-center">
          <div class="p-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Proyecto final de la carrera de Desarrollo Web</h2>
            <p class="text-gray-700 mb-6">
              Diseñado y programado por Manuel Salamanca
            </p>
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Tecnologias utilizadas</h2>
            <ul class="list-disc md:columns-5 columns-2 mx-6">
              <li class="flex items-center">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg" alt="Vue.js"
                  class="w-6 h-6 mr-2" /> Vue.js
              </li>
              <li class="flex items-center">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django"
                  class="w-6 h-6 mr-2" /> Django
              </li>
              <li class="flex items-center">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker"
                  class="w-6 h-6 mr-2" /> Docker
              </li>
              <li class="flex items-center">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="PostgresSQL"
                  class="w-6 h-6 mr-2" /> PostgreSQL
              </li>
              <li class="flex items-center">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/djangorest/djangorest-plain.svg" alt="Django Rest Framework"
                  class="w-6 h-6 mr-2" /> Django Rest
              </li>
            </ul>
          </div>
        </section>
      </div>
    </main>

  </div>
</template>

<script setup lang="ts">

</script>

<style scoped>
:root {
  --color-custom-green: #70EB4A;
  --color-custom-green-dark: #5AC93B;
  --color-custom-green-light: #8EF16E;
}

.text-custom-green {
  color: var(--color-custom-green);
}
</style>
