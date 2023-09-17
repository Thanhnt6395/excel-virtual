import enModule from './lang/en'
import vnModule from './lang/vn'

const state = () => ({
  currentLang: 'en',
  currentIcon: '',
  en: "./src/assets/icons/flag-usa.svg",
  vn: "./src/assets/icons/flag-vietnam.svg",
  module: 'enModule'
})

const getters = {
  langs: (state, getters) => {
    let res = []
    let langs = getters[`${state.module}/byPage`]('global')
    for (const [k, v] of Object.entries(langs)) {
      res.push({
        key: k,
        icon: state[k],
        label: v
      })
    }
    return res
  },
  currentIcon: (state) => {
    return state[state.currentLang]
  },
  byPage: (state, getters) => (page) => {
    return getters[`${state.module}/byPage`](page)
  }
}

const actions = {
  setCurrentLang ({commit, state}, lang) {
    state.currentLang = lang
    console.log({curr: state.currentLang})
    commit('changeCurrentLang', lang)
  }
}

const mutations = {
  changeCurrentLang (state, lang) {
    state.currentIcon = state[lang]
    state.module = lang == 'en' ? 'enModule' : 'vnModule'
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
  modules: {
    enModule,
    vnModule,
  }
}