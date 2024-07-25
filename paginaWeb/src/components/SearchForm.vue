<template>
    <div class="grid">
      <div class="w-100 d-flex justify-content-center">
        <form class="needs-validation" novalidate @submit.prevent="buscarClientes">
          <div class="row g-3">
            <div class="col-12">
              <label for="name" class="form-label">Nombre</label>
              <input type="text" class="form-control" v-model="name" placeholder="pepito" required>
            </div>
            <div class="col-12">
              <label for="email" class="form-label">Correo</label>
              <input type="email" class="form-control" v-model="email" placeholder="you@example.com">
            </div>
            <div class="col-12">
              <label for="city" class="form-labael">Ciudad</label>
              <input type="text" class="form-control" v-model="city" placeholder="Bogota D.C" required>
            </div>
            <div class="col-12">
              <label for="phone" class="form-label">Telefono</label>
              <input type="number" class="form-control" v-model="phone" placeholder="300555555">
            </div>
          </div>
        </form>
      </div>
      <div class="d-flex flex-column flex-md-row p-4 gap-4 py-md-5 align-items-center justify-content-center">
        <div class="list-group">
          <table class = "table table-striped table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Ciudad</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in filteredUsers" :key="user.id">
                <td>{{ user.id }}</td>
                <td>{{ user.nombre || 'N/A'}}</td>
                <td>{{ user.correo || 'N/A'}}</td>
                <td>{{ user.telefono || 'N/A' }}</td>
                <td>{{ user.ciudad || 'N/A' }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        users: [],  // Inicializa como un array vacío
        name: '',
        email: '',
        city: '',
        phone: ''
      };
    },
    computed: {
      //se filtran los usuarios en this users para ser mostrados
      filteredUsers() {
        return this.users.filter(user => {
          return (
            (!this.name.trim() || (user.nombre && user.nombre.toLowerCase().includes(this.name.trim().toLowerCase()))) &&
            (!this.email.trim() || (user.correo && user.correo.toLowerCase().includes(this.email.trim().toLowerCase()))) &&
            (!this.city.trim() || (user.ciudad && user.ciudad.toLowerCase().includes(this.city.trim().toLowerCase()))) &&
            (!this.phone.trim() || (user.telefono && user.telefono.toString().includes(this.phone.trim())))
          );
        });
      }
    },
    mounted() {
      // Intenta cargar los usuarios del almacenamiento local
      const storedUsers = localStorage.getItem('users');
      if (storedUsers) {
        this.users = JSON.parse(storedUsers);
      } else {
        // Si no hay datos en almacenamiento local, realiza una solicitud a la API
        axios
          .get('http://127.0.0.1:5000/users')
          .then(response => {
            this.users = response.data;
            // Guarda los usuarios en el almacenamiento local
            localStorage.setItem('users', JSON.stringify(this.users));
          })
          .catch(error => {
            console.error('Hubo un error al obtener los usuarios:', error);
          });
      }
    },
    methods: {
      buscarClientes() {
        // Filtrado ya se realiza automáticamente con la propiedad computed `filteredUsers`
        // Aquí puedes realizar otras acciones si es necesario
      }
    }
  };
</script>