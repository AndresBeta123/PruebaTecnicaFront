<template>
  <div class="row g-3">
    <div class="row g-3">
      <form class="needs-validation row g-3" novalidate @submit.prevent="buscarClientes">
        <div >
          <div class="col-12">
            <label for="name" class="form-label">Nombre</label>
            <input type="text" class="form-control" v-model="lookupName" placeholder="Pepito" required>
          </div>
          
        </div>
        <button type="submit" class="btn btn-primary mt-3">Buscar Cliente</button>
      </form>
      
    </div>
    <div class="d-flex flex-column flex-md-row p-4 gap-4 py-md-5 align-items-center justify-content-center">
      <div class="list-group">
        <table class="table table-striped table-bordered">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Fecha de Creación</th>
              <th>Fecha de Actualización</th>
              <th>Enlace</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in searchResults.items" :key="user.id">
              <td>{{ user.id }}</td>
              <td>{{ user.lookupName || 'N/A' }}</td>
              <td>{{ formatDate(user.createdTime) || 'N/A' }}</td>
              <td>{{ formatDate(user.updatedTime) || 'N/A' }}</td>
              <td><a :href="user.links[0].href" target="_blank">Ver detalles</a></td>
            </tr>
          </tbody>
        </table>
      </div>
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
      lookupName: '',
      searchResults: {},
      searchError: false
    };
  },
  methods: {
    buscarClientes() {
      //json que se enviara al api rest
      const params = {
        lookupName: this.lookupName
      };

      axios.get('http://127.0.0.1:5000/search', { params })
        .then(response => {
          console.log('Resultados de la búsqueda:', response.data);
          this.searchResults = response.data;
          this.searchError = false;
        })
        .catch(error => {
          console.error('Hubo un error al buscar el cliente:', error);
          this.searchResults = {};
          this.searchError = true;
        });
    },
    formatDate(dateString) {
      if (!dateString) return 'N/A';
      const date = new Date(dateString);
      return date.toLocaleDateString(); // Formato de fecha en formato local
    }
  }
};
</script>
