<template>
	<div class="">
		<b-form @submit.prevent="onSubmit">
			<template v-if="isAdmin">
				<name @userData="userData" :isAdmin="isAdmin" :edit="edit" />
				<hr />
				<personal-data
					@personalData="personalData"
					:isAdmin="isAdmin"
					:edit="edit"
				/>
				<hr />
				<medical-data
					@medicalData="medicalData"
					:isAdmin="isAdmin"
					:edit="edit"
				/>
				<hr />
				<kinship-data
					@kinshipData="kinshipData"
					:isAdmin="isAdmin"
					:edit="edit"
				/>
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
					<div class="float-right mt-2" v-show="edit">
						<hr />
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
	},
	components: {
		Name,
		PersonalData,
		MedicalData,
		KinshipData,
	},
	data() {
		return {
			data: {
				citizen: {
					user: {},
				},
			},
			isLoading: true,
			edit: true,
		};
	},
	created() {
		if (!this.isAdmin) {
			this.getUserProfile();
			this.edit = this.$route.name === 'user_profile' ? false : true;
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
			this.data.citizen.user = e;
			return e;
		},
		personalData(e) {
			this.data = Object.assign(this.data, e);
			return e;
		},
		medicalData(e) {
			this.data = Object.assign(this.data, e);
			return e;
		},
		kinshipData(e) {
			this.data = Object.assign(this.data, e);
			return e;
		},
		formatInput() {
			const user = this.data.citizen.user;
			const formData = new FormData();
			for (var key in this.data) {
				if (key == 'citizen') {
					for (var item in user) {
						formData.append(`citizen.user.${item}`, user[item]);
					}
				}
				formData.append(key, this.data[key]);
			}
			return formData;
		},
		async onSubmit() {
			await this.axios
				.post(`api/nininfo/`, this.formatInput(), {
					headers: {
						'content-type': 'multipart/form-data',
					},
				})
				.then(({ data }) => {
					console.log(data);
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
};
</script>
