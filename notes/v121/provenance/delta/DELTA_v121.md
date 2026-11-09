# Proposed v1.21 concept/relation delta

Base v1.20: 1044 concepts / 2051 relations. Added: **22 concepts, 57 relations** → 1066 / 2108.
No collisions with existing ids; every relation target exists; types, labels and axes are from the v1.20 vocabulary. `rank` is null: the build assigns it (existing order unchanged; new concepts follow their priority block). `_template` names the concept whose priority/ranking were copied; drop it on merge.

| id | label | template (priority) | relations |
|---|---|---|---|
| `signed_window_operator` | Theorem | `window_energy_ledger` (0.307) | refines → `window_energy_ledger`; refines → `weil_operator`; lives-in → `bulk_form_B_off_E0` |
| `pole_cancelled_chebyshev_ledger` | Theorem | `window_energy_ledger` (0.307) | refines → `window_energy_ledger`; related → `pole_plane` |
| `moment_parametrization_hardy_quarter` | Theorem | `bulk_form_B_off_E0` (0.347) | refines → `bulk_form_B_off_E0`; related → `hardy_constant_window_weil`; analogue-of → `one_cusp_three_readings` |
| `mass_counterterm_character_class` | Theorem | `spring_energy_counterterm_split` (0.307) | refines → `spring_energy_counterterm_split`; uses → `connes_trace`; contrasts-with → `tautology_boundary` |
| `small_window_poincare_bound` | Theorem | `certified_windows` (0.347) | refines → `certified_windows`; tests → `weil_positivity` |
| `prime_window_certificates` | Theorem | `certified_windows` (0.347) | refines → `certified_windows`; extends → `small_window_poincare_bound`; tests → `weil_positivity` |
| `e0_minima_grid_bias` | Numerical | `window_signature_numerical_witness` (0.365) | refines → `window_signature_numerical_witness`; contrasts-with → `prime_window_certificates` |
| `n2_deletion_ghost_control` | Numerical | `explicit_ghost_window` (0.4) | instance → `explicit_ghost_window`; constrains → `weil_positivity` |
| `one_negative_direction_certificate` | Theorem | `bordered_inertia_moment_criterion` (0.307) | instance → `bordered_inertia_moment_criterion`; refines → `pole_block_hyperbolic_plane`; refines → `haynsworth_pole_plane_split_windows` |
| `fe_fixed_boundary_class` | Theorem | `pole_block_hyperbolic_plane` (0.325) | refines → `pole_block_hyperbolic_plane`; uses → `functional_equation` |
| `formal_projection_restates_w` | Restatement | `tautology_boundary` (0.579) | restates → `weil_positivity`; related → `tautology_boundary`; contrasts-with → `hodge_index` |
| `arithmetic_class_map_requirements` | Open | `thermodynamic_J_direction` (0.165) | refines → `no_ghost_missing_piece`; uses → `hodge_index`; related → `mp_quadratic_rr`; related → `mp_castelnuovo`; tested_by → `one_negative_direction_certificate` |
| `pencil_discriminant_window_conic` | Theorem | `pole_block_hyperbolic_plane` (0.325) | refines → `pole_block_hyperbolic_plane`; related → `kahler_triple_polarization` |
| `k0_not_arakelov_degree` | Theorem | `arakelov` (0.452) | fails-for → `arakelov`; contrasts-with → `mass_counterterm_character_class` |
| `probe_response_identity` | Theorem | `passive_network_positive_real` (0.42) | refines → `passive_network_positive_real`; uses → `lagarias`; related → `passivity` |
| `dispersion_not_passivity` | Theorem | `anomalous_dispersion` (0.212) | refines → `anomalous_dispersion`; analogy → `telegrapher_distortionless`; fails-for → `passivity` |
| `signed_kyp_delay_line` | Theorem | `passivity` (0.6) | refines → `passivity`; uses → `pole_cancelled_chebyshev_ledger` |
| `prime_gap_block_obstruction` | Theorem | `passivity` (0.6) | fails-for → `passivity`; refines → `signed_kyp_delay_line` |
| `kms_half_kernel_not_response` | Theorem | `kms_bost_connes` (0.307) | refines → `kms_bost_connes`; contrasts-with → `probe_response_identity`; related → `graded_primon_gas` |
| `gamma_kernel_planck_ladder` | Analogy | `planck_ott_landsberg_reading` (0.226) | refines → `local_product_state_covariance`; analogue-of → `planck_ott_landsberg_reading` |
| `serre_derivative_cusp_correction` | Theorem | `e2_anomaly` (0.307) | refines → `e2_anomaly`; analogue-of → `serre_derivative_analogy` |
| `boundary_class_691` | Theorem | `index_691_weight12` (0.325) | refines → `index_691_weight12`; related → `one_cusp_three_readings`; related → `adjoint_691_eisenstein_not_cuspidal` |
