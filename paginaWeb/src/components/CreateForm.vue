<template>
  <div>
    <h2>Crear Cliente</h2>
    <form  class = "row g-3" @submit.prevent="crearCliente">
      <div class="row g-3">
        <div class="col-12">
          <label for="firstName" class="form-label">Primer Nombre</label>
          <input type="text" class="form-control" v-model="firstName" placeholder="Pepito" required>
        </div>
        <div class="col-12">
          <label for="lastName" class="form-label">Apellido</label>
          <input type="text" class="form-control" v-model="lastName" placeholder="Perez" required>
        </div>
      </div>
      <button type="submit" class="btn btn-primary mt-3">Crear Cliente</button>
    </form>
    <div v-if="createSuccess" class="alert alert-success mt-3" role="alert">
      Cliente creado correctamente. ID: {{ createdUser.id }}, Nombre: {{ createdUser.lookupName }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      createSuccess: false,
      createdUser: null
    };
  },
  methods: {
    crearCliente() {
      const payload = {
        //json que se enviara al api rest
        name: {
          first: this.firstName,
          last: this.lastName
        }
      };

      axios.post('http://127.0.0.1:5000/create', payload)
        .then(response => {
          console.log('Cliente creado:', response.data);
          this.createSuccess = true;
          this.createdUser = response.data;
          // Limpiar el formulario después de la creación exitosa
          this.firstName = '';
          this.lastName = '';
        })
        .catch(error => {
          console.error('Hubo un error al crear el cliente:', error);
          this.createSuccess = false;
          this.createdUser = null;
        });
    }
  }
};
</script>