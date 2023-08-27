<template>
  <section id="register" class=" relative h-[70vh]">
    <div class="container mx-auto mt-[10rem]">
      <!-- loading -->
      <!-- <div class="box-content p-4 sm:p-8 shadow-md m-auto flex" :class="[!isLoading ? 'hidden' : 'block']">
        <span class="relative flex h-5 w-5 mr-2">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-5 w-5 bg-sky-500"></span>
        </span>
        Processing
      </div> -->

      <!-- Message -->
      <div class="box-content p-4 sm:p-8 shadow-md m-auto" :class="[!registSuccess ? 'hidden' : 'block']">
        <div class=" mt-5 flex flex-col">
          <span class="text-blue-950 font-light text-left text-sm">
            We have just send you an email to verify your account.
          </span>
          <span class="text-blue-950 font-light text-left text-sm">
            Please verified to login.
          </span>
        </div>
      </div>

      <!-- content -->
      <div class="box-content p-4 sm:p-8 shadow-md m-auto" :class="[!registSuccess ? 'block' : 'hidden']">
        <h1 class=" text-blue-950 font-bold uppercase mb-2 text-center text-3xl">Register</h1>
        <h3 class=" text-blue-950 font-light mb-7 text-center text-xl">Create your account</h3>
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
          <div class=" col-span-1 relative">
            <input 
              type="text" name="" id="first_name" placeholder="First Name" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2 peer placeholder-transparent" 
              v-model="form['first_name']">
            <label 
              for="first_name" 
              class=" absolute top-[-0.75rem] left-[0.75rem] bg-white px-2 text-md text-gray-600 
                      transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400
                      peer-placeholder-shown:left-1 peer-placeholder-shown:top-[0.75rem]
                     peer-focus:text-md peer-focus:text-gray-600 peer-focus:left-[0.75rem] peer-focus:top-[-0.75rem]"
            >First Name</label>
          </div>
          <div class=" col-span-1 relative">
            <input 
              type="text" name="" id="last_name" placeholder="Last Name" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2 peer placeholder-transparent" 
              v-model="form['last_name']">
            <label 
              for="last_name" 
              class=" absolute top-[-0.75rem] left-[0.75rem] bg-white px-2 text-md text-gray-600 
                      transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400
                      peer-placeholder-shown:left-1 peer-placeholder-shown:top-[0.75rem]
                     peer-focus:text-md peer-focus:text-gray-600 peer-focus:left-[0.75rem] peer-focus:top-[-0.75rem]"
            >Last Name</label>
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
          <div class=" col-span-2 relative">
            <input 
              type="password" name="" id="repeat_password" placeholder="Repeat Password" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2 peer placeholder-transparent" :class="[!diffPassword ? 'bg-red-300' : '']" 
              v-model="form['repeat_password']" @input="onInput">
            <label 
              for="password" 
              class=" absolute top-[-0.75rem] left-[0.75rem] bg-white px-2 text-md text-gray-600 
                      transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400
                      peer-placeholder-shown:left-1 peer-placeholder-shown:top-[0.75rem]
                     peer-focus:text-md peer-focus:text-gray-600 peer-focus:left-[0.75rem] peer-focus:top-[-0.75rem]"
            >Repeat Password</label>
            <span class=" text-red-400 hidden" :class="[!validation.repeat_password ? ' peer-focus:block' : 'peer-focus:hidden']">
              Please enter more 8 characters for password
            </span>
          </div>
          <div class=" col-span-1">
            <input type="checkbox" name="" id="show-password" class=" mr-3" v-model="showPassword">
            <label for="show-password" class="text-blue-950 font-light">Show password</label>
          </div>
          <div class=" col-span-1 flex justify-end">
            <router-link to="/login" class="text-blue-950 font-light text-base hover:text-blue-600">Have an account ?</router-link>
          </div>
          <div class=" col-span-2 flex">
            <div class="flex" :class="[!isLoading ? 'hidden' : 'block']">
              <span class="relative flex h-5 w-5 mr-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-5 w-5 bg-sky-500"></span>
              </span>
              Processing...
            </div>
            <button 
              v-if="!isLoading"
              type="button" 
              class=" w-1/2 bg-blue-700 hover:bg-blue-500 text-white px-3 py-2 rounded uppercase mx-auto" 
              :class="[!allowClick ? 'opacity-50 cursor-not-allowed' : '']"  
              @click="register"
            >Register</button>
          </div>
        </div>
      </div>

      <!-- Notifications -->
      <div class=" absolute right-[2rem] bottom-0 transition-opacity transform duration-700 origin-left ease-linear" v-if="registStatus.status != ''">
        <Notifications :status="registStatus.status">{{ registStatus.message }}</Notifications>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import axios from 'axios';
import Notifications from '../components/Notifications.vue';

const form = ref({})
const validation = ref({})
const showPassword = ref(false)
const diffPassword = ref(true)
const allowClick = ref(true)
const isLoading = ref(false)
const registSuccess = ref(false)
const registStatus = ref({
  status: '',
  message: ''
})

watch(showPassword, (newValue) => {
  if (!newValue) {
    document.getElementById('password').setAttribute('type', 'password')
    document.getElementById('repeat_password').setAttribute('type', 'password')
  } else {
    document.getElementById('password').setAttribute('type', 'text')
    document.getElementById('repeat_password').setAttribute('type', 'text')
  }
})

watch(
  () => form.value.repeat_password, 
  (newValue) => {
  if (newValue && newValue != form.value.password) diffPassword.value = false
  else diffPassword.value = true
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
  if (!form.value.email || !form.value.password || !form.value.repeat_password) {
    if (!form.value.email) {
      validation.value.email = false
      document.getElementById('email').focus()
    }
    else if (!form.value.password) {
      validation.value.password = false
      document.getElementById('password').focus()
    }
    else {
      validation.value.repeat_password = false
      document.getElementById('repeat_password').focus()
    }
    allowClick.value = false
    return false
  }

  if (form.value.password != form.value.repeat_password) {
    allowClick.value = false
    return false
  }
  for (const [k, v] of Object.entries(form.value)) {
    if (['email', 'password', 'repeat_password'].includes(k) && !validation.value[k]) {
      allowClick.value = false
      return false
    }
  }
  return true
}

async function register() {
  if (!isValidation()) return false
  isLoading.value = true
  let formData = new FormData()
  for (const [k, v] of Object.entries(form.value)) {
    if (k == 'repeat_password') continue
    formData.append(k,v)
  }
  await axios.post('http://127.0.0.1:8000/api/user/register', formData)
    .then((res) => {
      console.log({res})
      if (res.status == 201) {
        registSuccess.value = true
        registStatus.value.status = 'success'
        registStatus.value.message = 'Email successfully registed!'
      }
    })
    .catch((error) => {
      console.log({error})
      if (error.response.status == 400) {
        registSuccess.value = false
        registStatus.value.status = 'error'
        registStatus.value.message = 'This email had used!'
      }
    })
  setTimeout(() => {
        // console.log("Delayed for 1 second.");
        registStatus.value.status = ''
        registStatus.value.message = ''
      }, "3000");
  isLoading.value = false
}

</script>

<style scoped>

</style>