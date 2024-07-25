<template>
  <div>
    <h2>Actualizar Cliente</h2>
    <form @submit.prevent="actualizarCliente">
      <div class="row g-3">
        <div class="col-12">
          <label for="userId" class="form-label">ID del Cliente</label>
          <input type="number" class="form-control" v-model="userId" placeholder="123" required>
        </div>
        <div class="col-12">
          <label for="firstName" class="form-label">Primer Nombre</label>
          <input type="text" class="form-control" v-model="firstName" placeholder="Tatiana" required>
        </div>
        <div class="col-12">
          <label for="lastName" class="form-label">Apellido</label>
          <input type="text" class="form-control" v-model="lastName" placeholder="Sanchez" required>
        </div>
        <div class="col-12">
          <label for="city" class="form-label">Ciudad</label>
          <input type="text" class="form-control" v-model="city" placeholder="Bogotá" required>
        </div>
        <button type="submit" class="btn btn-primary mt-3">Actualizar Cliente</button>
      </div>
    </form>
    <div v-if="updateSuccess" class="alert alert-success mt-3" role="alert">
      Cliente actualizado correctamente.
    </div>
    <div v-if="updateError" class="alert alert-danger mt-3" role="alert">
      Hubo un error al actualizar el cliente.
    </div>
  </div>
</template>

  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      userId: '',
      firstName: '',
      lastName: '',
      city: '',
      updateSuccess: false,
      updateError: false
    };
  },
  methods: {
    //json que se enviara al api rest
    actualizarCliente() {
      const payload = {
        id: this.userId,
        first_name: this.firstName,
        last_name: this.lastName,
        city: this.city
      };
      
      axios.patch('http://127.0.0.1:5000/update', payload)
        .then(response => {
          console.log('Cliente actualizado:', response.data);
          this.updateSuccess = true;
          this.updateError = false;
          // Limpiar el formulario después de la actualización exitosa
          this.userId = '';
          this.firstName = '';
          this.lastName = '';
          this.city = '';
        })
        .catch(error => {
          console.error('Hubo un error al actualizar el cliente:', error);
          this.updateSuccess = false;
          this.updateError = true;
        });
    }
  }
};
</script>
