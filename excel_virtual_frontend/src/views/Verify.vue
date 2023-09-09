<template>
  <section id="register" class=" relative h-[70vh]">
    <div class="container mx-auto mt-[10rem]">
      <div class="box-content p-4 sm:p-8 shadow-md m-auto">
        <h1 class=" text-blue-950 font-bold text-center text-2xl uppercase mb-7">{{ messages[status] }}</h1>
        <div class=" mt-5 flex justify-center" v-if="!isLoading">
          <button 
            type="button" 
            class=" uppercase bg-blue-600 text-white rounded-lg hover:bg-blue-400 py-3 px-4 w-fit" 
            @click="redirectLogin" v-if="status == 'success'"
          >Login</button>
          <button 
            v-else
            type="button" 
            class=" uppercase bg-blue-600 text-white rounded-lg hover:bg-blue-400 py-3 px-4 w-fit" 
            :class="[isSend.status != ''? 'hidden' : 'block']"
            @click="sendVerifyAgain"
          >Send verify again</button>
        </div>
        <div class="flex justify-center" :class="[status != 'success' && !isLoading ? 'block' : 'hidden']">
          <span class="relative flex h-5 w-5 mr-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-5 w-5 bg-sky-500"></span>
          </span>
          Sending...
        </div>
      </div>
    </div>

    <div class=" absolute right-[2rem] bottom-0 transition-opacity transform duration-700 origin-left ease-linear" v-if="isSend.status != ''">
      <Notifications :status="isSend.status">{{ isSend.message }}</Notifications>
    </div>
  </section>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import Notifications from '../components/Notifications.vue';

const router = useRouter()
const route = useRoute()
const status = route.params.status
const token = route.params.token
const messages = ref({
  success: 'Successfully Verified',
  expired: 'Token is Expired',
  decode: 'Token is valid',
  notFound: 'Email not exist'
})
const isLoading = ref(false)
const isSend = ref({
  status: '',
  message: ''
})

function redirectLogin() {
  router.push('/login')
}

async function sendVerifyAgain() {
  let formData = new FormData()
  formData.append('token', token)
  isLoading.value = true
  await axios.post('http://127.0.0.1:8000/api/user/verify-again', formData)
    .then((res) => {
      isSend.value.status = 'success'
      isSend.value.message = 'Verification Email send'
    })
    .catch((error) => {
      isSend.value.status = 'error'
      isSend.value.message = error.response.message
    })
  setTimeout(() => {
    isSend.value.status = ''
    isSend.value.message = ''
  }, "3000");
  isLoading.value = false
}

</script>

<style scoped>

</style>