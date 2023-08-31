<template>
  <section id="login" class=" relative h-[70vh]">
    <div class="container mx-auto mt-[10rem]">

      <!-- content -->
      <div class="box-content p-4 sm:p-8 shadow-md m-auto">
        <h1 class=" text-blue-950 font-bold uppercase mb-2 text-center text-3xl">Login</h1>
        <h3 class=" text-blue-950 font-light mb-7 text-center text-xl">Login your account</h3>
        <div class=" grid grid-cols-2 gap-x-3 gap-y-5">
          <div class=" col-span-2 relative">
            <input 
              type="text" name="" id="email" placeholder="Email" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2 peer placeholder-transparent" 
              v-model="form['email']" @input="onInput">
            <label 
              for="email" 
              class=" absolute top-[-0.75rem] left-[0.75rem] bg-white px-2 text-md text-gray-600 
                      transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400
                      peer-placeholder-shown:left-1 peer-placeholder-shown:top-[0.75rem]
                     peer-focus:text-md peer-focus:text-gray-600 peer-focus:left-[0.75rem] peer-focus:top-[-0.75rem]"
            >Email</label>
            <span class=" text-red-400 hidden" :class="[!validation.email ? ' peer-focus:block' : 'peer-focus:hidden']">
              Please enter a valid email address
            </span>
          </div>
          
          <div class=" col-span-2 relative">
            <input 
              type="password" name="" id="password" placeholder="Password" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2 peer placeholder-transparent" 
              v-model="form['password']" @input="onInput">
            <label 
              for="password" 
              class=" absolute top-[-0.75rem] left-[0.75rem] bg-white px-2 text-md text-gray-600 
                      transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400
                      peer-placeholder-shown:left-1 peer-placeholder-shown:top-[0.75rem]
                     peer-focus:text-md peer-focus:text-gray-600 peer-focus:left-[0.75rem] peer-focus:top-[-0.75rem]"
            >Password</label>
            <span class=" text-red-400 hidden" :class="[!validation.password ? ' peer-focus:block' : 'peer-focus:hidden']">
              Please enter more 8 characters for password
            </span>
          </div>
          
          <div class=" col-span-1">
            <input type="checkbox" name="" id="show-password" class=" mr-3" v-model="showPassword">
            <label for="show-password" class="text-blue-950 font-light">Show password</label>
          </div>
          <div class=" col-span-1 flex justify-end">
            <router-link to="/register" class="text-blue-950 font-light text-base hover:text-blue-600">Create an account ?</router-link>
          </div>
          <div class=" col-span-2 flex">
            <div class="flex" :class="[!isLoading ? 'hidden' : 'block']">
              <span class="relative flex h-5 w-5 mr-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-5 w-5 bg-sky-500"></span>
              </span>
              Logining...
            </div>
            <button 
              v-if="!isLoading"
              type="button" 
              class=" w-1/2 bg-blue-700 hover:bg-blue-500 text-white px-3 py-2 rounded uppercase mx-auto" 
              :class="[!allowClick ? 'opacity-50 cursor-not-allowed' : '']"  
              @click="login"
            >Login</button>
          </div>
        </div>
      </div>

      <!-- Notifications -->
      <div class=" absolute right-[2rem] bottom-0 transition-opacity transform duration-700 origin-left ease-linear" v-if="loginStatus.status != ''">
        <Notifications :status="loginStatus.status">{{ loginStatus.message }}</Notifications>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import axios from 'axios';
import Notifications from '../components/Notifications.vue';
import { useRouter } from 'vue-router';

const form = ref({})
const router = useRouter()
const validation = ref({})
const showPassword = ref(false)
const allowClick = ref(true)
const isLoading = ref(false)
const loginStatus = ref({
  status: '',
  message: ''
})

watch(showPassword, (newValue) => {
  if (!newValue) {
    document.getElementById('password').setAttribute('type', 'password')
  } else {
    document.getElementById('password').setAttribute('type', 'text')
  }
})

function onInput(e) {
  let id = e.target.id
  let value = e.target.value
  if (!allowClick.value) allowClick.value = true
  if (id == 'email') validation.value.email = isEmail(value)
  else if (id.includes('password')) validation.value[id] = value.length < 8 ? false : true
}

function isEmail(email) {
  if (!email || email == '') return false
  const regex = new RegExp("^[\\w-_\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$")
  return regex.test(email)
}

function isValidation() {
  if (!form.value.email || !form.value.password) {
    if (!form.value.email) {
      validation.value.email = false
      document.getElementById('email').focus()
    } else {
      validation.value.password = false
      document.getElementById('password').focus()
    }
    allowClick.value = false
    return false
  }

  for (const [k, v] of Object.entries(form.value)) {
    if (['email', 'password'].includes(k) && !validation.value[k]) {
      allowClick.value = false
      return false
    }
  }
  return true
}

async function login() {
  if (!isValidation()) return false
  isLoading.value = true
  let formData = new FormData()
  for (const [k, v] of Object.entries(form.value)) {
    formData.append(k,v)
  }

  await axios.post('http://127.0.0.1:8000/api/user/login', formData)
    .then((res) => {
      console.log({res})
      if (res.status == 200) {
        router.push('/')
      }
    })
    .catch((error) => {
      console.log({error})
      loginStatus.value.status = 'error'
      loginStatus.value.message = error.response.data.detail
    })

  setTimeout(() => {
    loginStatus.value.status = ''
    loginStatus.value.message = ''
  }, "3000");
  isLoading.value = false
}

</script>

<style scoped>

</style>