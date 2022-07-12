<template>
	<div>
		<header-vue />
		<b-row>
			<b-col md="2">
				<sidebar-vue :userType="userType" />
			</b-col>
			<b-col md="10">
				<b-card title="NIN Documents" class="mt-3">
					<b-tabs
						content-class="mt-3 w-75 mx-auto"
						justified
						v-model="tabIndex"
					>
						<b-tab title="Education" active>
							<get-education-vue :user="user" />
						</b-tab>
						<b-tab title="Professional">
							<get-professional :user="user"
						/></b-tab>
						<b-tab title="CV"> <get-cv :user="user" /></b-tab>
						<b-tab title="Certificate"> <get-certificate :user="user" /></b-tab>
					</b-tabs>
				</b-card>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '@/components/header/Header.vue';
import SidebarVue from '@/components/sidebar/Sidebar.vue';
import GetEducationVue from '@/components/documents/education/GetEducation.vue';
import GetCertificate from '@/components/documents/certificate/GetCertificate.vue';
import GetProfessional from '@/components/documents/professional/GetProfessional.vue';
import GetCv from '@/components/documents/cv/GetCV.vue';
export default {
	name: 'PatnerDocument',
	components: {
		HeaderVue,
		SidebarVue,
		GetEducationVue,
		GetCertificate,
		GetProfessional,
		GetCv,
	},
	data() {
		return {
			tabIndex: null,
			user: {},
			userType: 'patner',
		};
	},
	created() {
		const userData = JSON.parse(localStorage.getItem('nininfo'));
		this.user = userData.citizen.user;
	},
};
</script>
