<template>
    <div class="min-h-screen bg-gray-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8">
            <div>
                <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                    Regístrate en RAPITURNO
                </h2>
                <p class="mt-2 text-center text-sm text-gray-600">
                    ¿Ya tienes una cuenta?
                    <router-link :to="{ name: 'login' }"
                        class="font-medium text-custom-green hover:text-custom-green-dark">
                        Inicia sesión aquí
                    </router-link>
                </p>
            </div>
            <form class="mt-8 space-y-6" @submit.prevent="handleSubmit">
                <div class="space-y-6">
                    <div>
                        <label for="username" class="block text-sm font-medium text-gray-700">Nombre de usuario</label>
                        <input id="username" name="username" type="text" required
                            class="mt-1 appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-custom-green focus:border-custom-green focus:z-10 sm:text-sm"
                            v-model="username" />
                    </div>
                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700">Correo electrónico</label>
                        <input id="email" name="email" type="email" autocomplete="email" required
                            class="mt-1 appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-custom-green focus:border-custom-green focus:z-10 sm:text-sm"
                            v-model="email" />
                    </div>
                    <div>
                        <label for="first-name" class="block text-sm font-medium text-gray-700">Nombre</label>
                        <input id="first-name" name="first-name" type="text" required
                            class="mt-1 appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-custom-green focus:border-custom-green focus:z-10 sm:text-sm"
                            v-model="firstName" />
                    </div>
                    <div>
                        <label for="last-name" class="block text-sm font-medium text-gray-700">Apellido</label>
                        <input id="last-name" name="last-name" type="text" required
                            class="mt-1 appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-custom-green focus:border-custom-green focus:z-10 sm:text-sm"
                            v-model="lastName" />
                    </div>
                    <div>
                        <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
                        <input id="password" name="password" type="password" autocomplete="new-password" required
                            class="mt-1 appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-custom-green focus:border-custom-green focus:z-10 sm:text-sm"
                            v-model="password" minlength="8" maxlength="25" />
                    </div>
                    <div>
                        <label for="password-confirm" class="block text-sm font-medium text-gray-700">Confirmar
                            contraseña</label>
                        <input id="password-confirm" name="password-confirm" type="password" autocomplete="new-password"
                            required
                            class="mt-1 appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-custom-green focus:border-custom-green focus:z-10 sm:text-sm"
                            maxlength="25" v-model="passwordConfirm" />
                    </div>
                </div>

                <div v-if="error" class="text-red-600 text-sm text-center mt-2">
                    {{ error }}
                </div>

                <div>
                    <button type="submit"
                        class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-black bg-custom-green hover:bg-custom-green-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-custom-green">
                        <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                        </span>
                        Registrarse
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ElMessage } from 'element-plus';
import { onMounted, ref, type Ref } from 'vue';
import router from '@/router';
import store from '@/stores/login';
const AuthUser = store();
const username: Ref<string> = ref('')
const email: Ref<string> = ref('')
const firstName: Ref<string> = ref('')
const lastName: Ref<string> = ref('')
const password: Ref<string> = ref('')
const passwordConfirm: Ref<string> = ref('')
const error = ref('')
const handleSubmit = () => {
    // Validación básica
    if (password.value !== passwordConfirm.value) {
        ElMessage({
            showClose: true,
            duration: 5 * 1000,
            type: 'error',
            message: 'Las contraseñas no coinciden'
        })
    } else {
        registro()
    }
    // Aquí iría la lógica para manejar el registro

    // Resetear el error si todo está bien
    error.value = ''
}
const registro = async () => {
        const response = await AuthUser.register(username.value, email.value, password.value, passwordConfirm.value, lastName.value, firstName.value);
        if (!response.success) {
            ElMessage({
                showClose: true,
                duration: 5 * 1000,
                type: 'error',
                message: 'error al registrarse intente de nuevo mas tarde'
            })
        } else {
            ElMessage({
                showClose: true,
                duration: 5 * 1000,
                type: 'success',
                message: 'Cuenta creada con éxito',
            })
            router.push('/login')
        }
    }
</script>
<style scoped></style>
