<template>
    <div class="grid">
      <div>
        <form class="needs-validation" novalidate @submit.prevent="buscarCliente">
          <div>
            <div class="col-12">
              <label for="id" class="form-label">ID del Cliente</label>
              <input type="text" class="form-control" v-model="contactId" placeholder="ID del Cliente" required>
            </div>
          </div>
          <button type="submit" class="btn btn-primary mt-3 w100 d-flex justify-content-center">Buscar Cliente</button>
        </form>
      </div>
      <div v-if="searchResults">
        <table class="table table-striped table-bordered">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Ciudad</th>
              <th>Correo</th>
              <th>Teléfono</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ searchResults.id }}</td>
              <td>{{ searchResults.nombre || 'N/A' }}</td>
              <td>{{ searchResults.ciudad || 'N/A' }}</td>
              <td>{{ searchResults.correo || 'N/A' }}</td>
              <td>{{ searchResults.telefono || 'N/A' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-if="searchError" class="alert alert-danger mt-3" role="alert">
        Hubo un error al buscar el cliente.
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        contactId: '',
        searchResults: null,
        searchError: false
      };
    },
    methods: {
      buscarCliente() {
        axios.get(`http://127.0.0.1:5000/searchById/${this.contactId}`)
          .then(response => {
            this.searchResults = response.data;
            this.searchError = false;
          })
          .catch(error => {
            console.error('Hubo un error al buscar el cliente:', error);
            this.searchResults = null;
            this.searchError = true;
          });
      }
    }
  };
  </script>
  