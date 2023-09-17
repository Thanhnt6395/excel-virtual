const enMessages = {
  global: {
    en: 'English',
    vn: 'Vietnamese',
  },
  homepage: {
    _new: 'New Spreadsheet',
    myFile: 'My sheets',
    _search: 'Search',
  }
}

export default {
  namespaced: true,
  state: () => ({
    messages: enMessages,
  }),
  getters: {
    all: state => state.messages,
    byPage: (state) => (page) => {
      return state.messages[page]
    },
    byDetail: (state, getters) => (page, detail) => {
      return getters.byPage(page)[detail]
    }
  }
}