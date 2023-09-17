import axios from "axios";

const axiosClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    withCredentials: true,
  });

  // axiosClient.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

  export default axiosClient;