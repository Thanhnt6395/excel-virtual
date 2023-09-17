const vnMessages = {
  global: {
    en: 'Tiếng Anh',
    vn: 'Tiếng Việt',
  },
  homepage: {
    _new: 'Tạo spreadsheet mới',
    myFile: 'Sheets của tôi',
    _search: 'Tìm kiếm',
  }
}

export default {
  namespaced: true,
  state: () => ({
    messages: vnMessages,
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