import axiosClient from "../../utils/Axios"

const state = () => ({
  user: {},
  sheets: [],
  jwt: null,
})

const getters = {}

const actions = {
  async getUser ({commit, state}) {
    await axiosClient.get('/user/view')
      .then((res) => {
        console.log({res})
        if (res.status == 200) {
          commit('getUser', res.data)
        }
      })
      .catch((error) => {
        commit('getUser', {})
      })
  },
}

const mutations = {
  getUser (state, data) {
    state.user = data
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}