<template>
  <section id="register">
    <div class="container mx-auto mt-[10rem]">
      <div class="box-content p-4 sm:p-8 shadow-md m-auto">
        <h1 class=" text-blue-950 font-bold uppercase mb-2 text-center text-3xl">Register</h1>
        <h3 class=" text-blue-950 font-light mb-7 text-center text-xl">Create your account</h3>
        <div class=" grid grid-cols-2 gap-x-3 gap-y-5">
          <div class=" col-span-2 relative">
            <label for="email" :class="[showLabel.email ? 'visible absolute top-[-0.5rem] left-[1rem] bg-white px-1': 'invisible']">Email</label>
            <input 
              type="text" name="" id="email" placeholder="Email" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2" 
              v-model="form['email']" @input="onInput">
          </div>
          <div class=" col-span-1">
            <label for="first_name" :class="[showLabel.first_name ? 'visible absolute top-[-0.5rem] left-[1rem] bg-white px-1': 'invisible']">First Name</label>
            <input 
              type="text" name="" id="first_name" placeholder="First Name" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2" 
              v-model="form['first_name']" @input="onInput">
          </div>
          <div class=" col-span-1">
            <label for="last_name" :class="[showLabel.last_name ? 'visible absolute top-[-0.5rem] left-[1rem] bg-white px-1': 'invisible']">Last Name</label>
            <input 
              type="text" name="" id="last_name" placeholder="Last Name" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2" 
              v-model="form['last_name']" @input="onInput">
          </div>
          <div class=" col-span-2">
            <label for="password" :class="[showLabel.password ? 'visible absolute top-[-0.5rem] left-[1rem] bg-white px-1': 'invisible']">Password</label>
            <input 
              type="password" name="" id="password" placeholder="Password" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2" 
              v-model="form['password']" @input="onInput">
          </div>
          <div class=" col-span-2">
            <label for="repeat_password" :class="[showLabel.repeat_password ? 'visible absolute top-[-0.5rem] left-[1rem] bg-white px-1': 'invisible']">Repeat Password</label>
            <input 
              type="password" name="" id="repeat_password" placeholder="Repeat Password" 
              class=" border border-gray-200 rounded w-full h-[3rem] px-3 py-2" 
              v-model="form['repeat_password']" @input="onInput">
          </div>
          <div class=" col-span-1">
            <input type="checkbox" name="" id="show-password" class=" mr-3">
            <label for="show-password" class="text-blue-950 font-light">Show password</label>
          </div>
          <div class=" col-span-1 flex justify-end">
            <router-link to="/login" class="text-blue-950 font-light text-base hover:text-blue-600">Have an account ?</router-link>
          </div>
          <div class=" col-span-2 flex">
            <button type="button" class=" w-1/2 bg-blue-700 hover:bg-blue-500 text-white px-3 py-2 rounded uppercase mx-auto">Register</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue';

const form = ref({})
const showLabel = ref({
  email: false,
  first_name: false,
  last_name: false,
  password: false,
  repeat_password: false
})

function onInput(e) {
  let id = e.target.id
  if (!form.value[id] || form.value[id] == '') showLabel.value[id] = false
  else showLabel.value[id] = true
}

</script>

<style scoped>

</style>