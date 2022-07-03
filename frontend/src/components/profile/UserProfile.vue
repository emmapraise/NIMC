<template>
	<div class="">
		<template v-if="isAdmin">
			<b-form @submit.prevent="onSubmit">
				<name @userData="userData" />
				<hr />
				<personal-data @personalData="personalData" />
				<hr />
				<medical-data @medicalData="medicalData" />
				<hr />
				<kinship-data @kinshipData="kinshipData" />
				<div class="float-right mt-2">
					<b-button type="submit" variant="success">Submit</b-button>
				</div>
			</b-form>
		</template>
		<template v-else>
			<div v-if="isLoading" class="d-flex justify-content-center mb-3">
				<b-spinner
					type="grow"
					variant="info"
					style="width: 3rem; height: 3rem"
					label="loading"
				/>
			</div>
			<div v-else>
				<name :getData="data" :isAdmin="isAdmin" />
				<hr />
				<personal-data :getData="data" :isAdmin="isAdmin" />
				<hr />
				<medical-data :getData="data" :isAdmin="isAdmin" />
				<hr />
				<kinship-data :getData="data" :isAdmin="isAdmin" />
			</div>
		</template>
	</div>
</template>
<script>
import Name from '../info/Name.vue';
import PersonalData from '../info/PersonalData.vue';
import MedicalData from '../info/MedicalData.vue';
import KinshipData from '../info/KinshipData.vue';
export default {
	name: 'RegisterView',
	props: ['isAdmin'],
	components: {
		Name,
		PersonalData,
		MedicalData,
		KinshipData,
	},
	data() {
		return {
			data: {},
			isLoading: true,
			userDispatch: {
				user: {},
			},
		};
	},
	created() {
		console.log('admins', this.isAdmin);
		if (!this.isAdmin) {
			this.getUserProfile();
		}
	},
	mounted() {},
	methods: {
		getUserProfile() {
			const user = JSON.parse(this.$store.state.user);
			this.axios
				.get(`api/nininfo/${user.id}/`)
				.then(({ data }) => {
					console.log('data', data);
					this.data = data;

					this.isLoading = false;
				})
				.catch((err) => {
					console.log(err);
				});
		},
		userData(e) {
			console.log(e);
		},
		personalData(e) {
			console.log(e);
		},
		medicalData(e) {
			console.log(e);
		},
		kinshipData(e) {
			console.log(e);
		},
		onSubmit() {
			console.log(this.data);
		},
	},
};
</script>
