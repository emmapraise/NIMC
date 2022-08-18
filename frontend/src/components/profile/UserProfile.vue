<template>
	<div class="">
		<template v-if="isAdmin">
			<b-form @submit.prevent="onSubmit">
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
			</b-form>
		</template>

		<template v-else>
			<b-alert
				:show="dismissCountDown"
				dismissible
				variant="success"
				@dismissed="dismissCountDown = 0"
				@dismiss-count-down="countDownChanged"
			>
				<p>Update Request Successful</p>
			</b-alert>
			<b-form @submit.prevent="onUpdate">
				<div v-if="isLoading" class="d-flex justify-content-center mb-3">
					<b-spinner
						type="grow"
						variant="info"
						style="width: 3rem; height: 3rem"
						label="loading"
					/>
				</div>
				<div v-else>
					<name
						@userData="userData"
						:getData="data"
						:isAdmin="isAdmin"
						:edit="edit"
					/>
					<hr />
					<personal-data
						:getData="data"
						:isAdmin="isAdmin"
						:edit="edit"
						@personalData="personalData"
					/>
					<hr />
					<medical-data
						:getData="data"
						:isAdmin="isAdmin"
						:edit="edit"
						@medicalData="medicalData"
					/>
					<hr />
					<kinship-data
						:getData="data"
						:isAdmin="isAdmin"
						:edit="edit"
						@kinshipData="kinshipData"
					/>
					<div class="float-right mt-2" v-show="edit">
						<hr />
						<!-- <b-button variant="success" @click="handleOk"> Update </b-button> -->
						<b-button type="submit" variant="success">Update</b-button>
					</div>
				</div>
				<b-modal
					id="modal-1"
					@ok="handleOk"
					ref="modal"
					title="Upload Court Afidavit"
				>
					<b-form-file
						v-model="document"
						:state="Boolean(document)"
						placeholder="Choose a file or drop it here..."
						drop-placeholder="Drop file here..."
					></b-form-file>
				</b-modal>
			</b-form>
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
			dismissSecs: 5,
			dismissCountDown: 0,
			showDismissibleAlert: false,
			document: null,
			data: {
				citizen: {
					user: {},
				},
			},
			isLoading: true,
			edit: true,
		};
	},
	created() {},
	mounted() {
		this.getEditMode();
	},
	methods: {
		countDownChanged(dismissCountDown) {
			this.dismissCountDown = dismissCountDown;
		},
		handleOk() {
			const formData = new FormData();
			formData.append('document', this.document);

			this.axios
				.patch(`api/update-nininfo/${this.data.id}/`, formData, {
					headers: {
						'content-type': 'multipart/form-data',
					},
				})
				.then(() => {
					this.showAlert();
					setTimeout(this.$router.push({ name: 'user_profile' }), 10000);
				})
				.catch((err) => {
					console.log(err);
				});
		},
		showAlert() {
			this.dismissCountDown = this.dismissSecs;
		},
		getEditMode() {
			if (
				this.$route.name === 'make_request' ||
				this.$route.name === 'user_profile'
			) {
				this.getUserProfile();
				this.edit = this.$route.name === 'user_profile' ? false : true;
			}
		},
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
					this.$router.push({
						name: 'enrolment_success',
						params: { user: data.citizen.user },
					});
				})
				.catch((err) => {
					console.log(err);
				});
		},
		async onUpdate() {
			this.data.citizen = this.data.citizen.id;
			this.data.nin_info = this.data.id;
			await this.axios
				.post(`api/update-nininfo/`, this.data, {
					headers: {
						'content-type': 'application/json',
					},
				})
				.then(({ data }) => {
					this.data = data;
					this.$root.$emit('bv::show::modal', 'modal-1', '#btnShow');
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
};
</script>
