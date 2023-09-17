import { createStore, createLogger } from 'vuex'
import user from './modules/user'
import messages from './modules/messages'

// const debug = process.env.NODE_ENV !== 'production'

export default createStore({
  modules: {
    user,
    messages
  },
  // strict: debug,
  // plugins: debug ? [createLogger()] : []
})