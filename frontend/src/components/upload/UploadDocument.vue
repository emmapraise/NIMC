<template>
	<div>
		<b-tabs
			content-class="mt-3 w-75 mx-auto"
			justified
			v-model="tabIndex"
			v-if="!isLoading"
		>
			<b-tab title="Education" active>
				<template v-if="user.is_admin">
					<upload-education-vue :nininfo="results"
				/></template>
				<template v-else> <get-education-vue :user="user" /></template>
			</b-tab>
			<b-tab title="CV">
				<cv-vue :nininfo="results" />
			</b-tab>
			<b-tab title="Professional Document">
				<template v-if="user.is_admin">
					<upload-professional :nininfo="results" />
				</template>
				<template v-else>
					<get-professional-vue :user="user" />
				</template>
			</b-tab>
			<b-tab title="Certificates">
				<template v-if="user.is_admin">
					<upload-certificate-vue :nininfo="results" />
				</template>
				<template v-else>
					<get-certificate-vue :user="user" />
				</template>
			</b-tab>
		</b-tabs>
		<div v-else class="d-flex justify-content-center mb-3">
			<b-spinner
				type="grow"
				variant="info"
				style="width: 3rem; height: 3rem"
				label="loading"
			/>
		</div>
	</div>
</template>
<script>
import UploadEducationVue from '../documents/education/UploadEducation.vue';
import GetEducationVue from '../documents/education/GetEducation.vue';
import CvVue from '../documents/Cv.vue';
import UploadCertificateVue from '../documents/certificate/UploadCertificate.vue';
import GetCertificateVue from '../documents/certificate/GetCertificate.vue';
import UploadProfessional from '../documents/professional/UploadProfessional.vue';
import GetProfessionalVue from '../documents/professional/GetProfessional.vue';
export default {
	name: 'UploadDocumentComponent',
	components: {
		UploadEducationVue,
		GetEducationVue,
		CvVue,
		UploadProfessional,
		UploadCertificateVue,
		GetCertificateVue,
		GetProfessionalVue,
	},
	data() {
		return {
			results: [],
			isLoading: true,
			tabIndex: null,
			user: {},
		};
	},
	created() {
		this.user = JSON.parse(localStorage.getItem('user'));
		this.getCitizen();
	},
	methods: {
		async getCitizen() {
			await this.axios
				.get(`api/nininfo/`)
				.then(({ data }) => {
					this.results = data.results;
					this.isLoading = false;
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
};
</script>
