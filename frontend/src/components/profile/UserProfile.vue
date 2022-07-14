<template>
	<div class="">
		<b-form @submit.prevent="onSubmit">
			<template v-if="isAdmin">
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
					<name :getData="data" :isAdmin="isAdmin" :edit="edit" />
					<hr />
					<personal-data :getData="data" :isAdmin="isAdmin" :edit="edit" />
					<hr />
					<medical-data :getData="data" :isAdmin="isAdmin" :edit="edit" />
					<hr />
					<kinship-data :getData="data" :isAdmin="isAdmin" :edit="edit" />
					<hr />
					<div class="float-right mt-2" v-show="edit">
						<b-button type="submit" variant="success">Update</b-button>
					</div>
				</div>
			</template>
		</b-form>
	</div>
</template>
<script>
import Name from '../info/Name.vue';
import PersonalData from '../info/PersonalData.vue';
import MedicalData from '../info/MedicalData.vue';
import KinshipData from '../info/KinshipData.vue';
export default {
	name: 'RegisterView',
	props: {
		isAdmin: Boolean,
		edit: Boolean,
	},
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
		};
	},
	created() {
		if (!this.isAdmin) {
			this.getUserProfile();
		}
	},
	mounted() {},
	methods: {
		async getUserProfile() {
			const user = JSON.parse(localStorage.getItem('user'));
			await this.axios
				.get(`api/nininfo/${user.id}/`)
				.then(({ data }) => {
					this.data = data;

					this.isLoading = false;
				})
				.catch(() => {});
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
